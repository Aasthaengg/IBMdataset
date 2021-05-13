import sys
from math import factorial
MOD = 10**9+7
h, w, k = [int(i) for i in sys.stdin.readline().split()]
# memo_ls[n] : n本の平行線に対し、あみだくじの条件を満たす組み合わせの数
memo_ls2 = [[0 for x in range(2)] for y in range(8)]
memo_ls2[1][0] = 1
for i in range(2,8):
    memo_ls2[i][0] = memo_ls2[i-1][1] + memo_ls2[i-1][0]
    memo_ls2[i][1] = memo_ls2[i-1][0]
memo_ls = [sum(i) for i in memo_ls2]
# memo_ls3[j][i] : j番目にiにいる通り数
memo_ls3 = [[0 for i in range(w)] for j in range(h+1)]
memo_ls3[0][0] = 1
for j in range(1,h+1):
    for i in range(w):
        if i > 0:
            memo_ls3[j][i] += memo_ls3[j-1][i-1] * memo_ls[max(1, i-1)] * memo_ls[max(1, w-1-i)]
        if i < w-1:
            memo_ls3[j][i] += memo_ls3[j - 1][i + 1] * memo_ls[max(1, i)] * memo_ls[max(1, w-i-2)]
        memo_ls3[j][i] += memo_ls3[j-1][i] * memo_ls[max(1, i)] * memo_ls[max(1, w-i-1)]
        memo_ls3[j][i] %= MOD
print(memo_ls3[-1][k-1])