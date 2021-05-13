import sys
from collections import Counter
INF = 10**18
N, K = [int(i) for i in sys.stdin.readline().split()]
len_k = len(bin(K)[2:])
A_ls = [bin(int(i))[2:] for i in sys.stdin.readline().split()]
max_len = max([len(i) for i in A_ls] + [len_k])
K = bin(K)[2:].zfill(max_len)
A_ls = [A.zfill(max_len) for A in A_ls]
# i番目の解
memo_ls = [0 for i in range(max_len)]
# i番目のみの最適解を考えた時の和
memo_ls2 = [0 for i in range(max_len)]
for i in range(max_len):
    ct = Counter([A[-1-i] for A in A_ls])
    # i番目のけたとして0を選んだ時の和
    ans_0 = 2**i*ct["1"]
    ans_1 = 2**i*ct["0"]
    ct.clear()
    memo_ls[-1-i] = (ans_0, ans_1)
    memo_ls2[-1-i] = max(ans_0, ans_1)
# i-1番目までの解の最大
# memo_ls3[i][j] j : 答えが決まっている時1, いない時0
memo_ls3 = [[0 for i in range(2)] for i in range(max_len + 1)]
memo_ls3[0][1] = -INF
for i, j in enumerate(K, 1):
    if j == "0":
        memo_ls3[i][0] = memo_ls3[i-1][0] + memo_ls[i-1][0]
        memo_ls3[i][1] = memo_ls3[i-1][1] + memo_ls2[i-1]
    else:
        memo_ls3[i][0] = memo_ls3[i-1][0] + memo_ls[i-1][1]
        memo_ls3[i][1] = max(memo_ls3[i-1][1] + memo_ls2[i-1], memo_ls3[i-1][0] + memo_ls[i-1][0])
res = max(memo_ls3[-1])
print(int(res))