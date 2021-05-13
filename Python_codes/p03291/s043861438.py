import sys
s = input()
mod = 10**9+7
memo_ls = [[0 for j in range(4)] for i in range(len(s) + 1)]
memo_ls[0][0] = 1
for i, _s in enumerate(s, 1):
    memo_ls[i][0] = memo_ls[i-1][0]
    memo_ls[i][1] = memo_ls[i-1][1]
    memo_ls[i][2] = memo_ls[i-1][2]
    memo_ls[i][3] = memo_ls[i - 1][3]
    if _s == "A":
        memo_ls[i][1] += memo_ls[i-1][0]
    elif _s == "B":
        memo_ls[i][2] += memo_ls[i-1][1]
    elif _s == "C":
        memo_ls[i][3] += memo_ls[i-1][2]
    else:
        memo_ls[i][0] *= 3
        memo_ls[i][1] *= 3
        memo_ls[i][2] *= 3
        memo_ls[i][3] *= 3
        memo_ls[i][1] += memo_ls[i - 1][0]
        memo_ls[i][2] += memo_ls[i - 1][1]
        memo_ls[i][3] += memo_ls[i - 1][2]
    memo_ls[i][0] %= mod
    memo_ls[i][1] %= mod
    memo_ls[i][2] %= mod
    memo_ls[i][3] %= mod
print(memo_ls[-1][-1] % mod)