N = int(input())
dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
for i in range(4):
    for j in range(4):
        for k in range(4):
            if k == 1 and j == 0 and i == 2:
                pass
            elif k == 0 and j == 2 and i == 1:
                pass
            elif k == 0 and j == 1 and i == 2:
                pass
            else:
                dp[3][i][j][k] = 1
mod = 10**9 + 7

for i in range(4, N + 1):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                for p in range(4):
                    if l == 1 and k == 0 and j == 2:
                        pass
                    elif l == 0 and k == 2 and j == 1:
                        pass
                    elif l == 0 and k == 1 and j == 2:
                        pass
                    elif p == 0 and k == 1 and j == 2:
                        pass
                    elif p == 0 and l == 1 and j == 2:
                        pass
                    else:
                        dp[i][j][k][l] += (dp[i - 1][k][l][p]) % mod

ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            ans += dp[N][i][j][k]

print(ans%mod)