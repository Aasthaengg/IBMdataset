import sys
n, k = [int(i) for i in sys.stdin.readline().split()]
a_ls = [int(i) for i in sys.stdin.readline().split()]
memo_ls = [-1 for i in range(k+1)]
memo_ls[0] = -1
for i in range(1, k+1):
    for a in a_ls:
        if a > i:
            continue
        memo_ls[i] = max(memo_ls[i - a] * (-1), memo_ls[i])
ans = ["","First", "Second"]
print(ans[memo_ls[-1]])