N = int(input())
mod = 10 ** 9 + 7

dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for i in range(N + 1)]

def judge(i, j, k):
    if i == 0 and j == 2 and k == 1:
        return False
    elif i == 0 and j == 1 and k == 2:
        return False
    elif i == 2 and j == 0 and k == 1:
        return False
    else:
        return True

for i in range(4):
    for j in range(4):
        for k in range(4):
            dp[3][i][j][k] = judge(i, j, k)

def judge(j, k, l, m):
    if k == 0 and l == 2 and m == 1:
        return False
    elif k == 0 and l == 1 and m == 2:
        return False
    elif k == 2 and l == 0 and m == 1:
        return False
    elif j == 0 and l == 2 and m == 1:
        return False
    elif j == 0 and k == 2 and m == 1:
        return False
    else:
        return True

for i in range(4, N + 1):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                for m in range(4):
                    dp[i][k][l][m] += dp[i - 1][j][k][l] * judge(j, k, l, m)
                    dp[i][k][l][m] %= mod
ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            ans += dp[N][i][j][k]
            ans %= mod
print(ans % mod)