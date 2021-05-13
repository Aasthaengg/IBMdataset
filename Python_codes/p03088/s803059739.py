N = int(input())
mod = 10**9+7

dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
dp[0][3][3][3] = 1
for i in range(N):
    for a in range(4):
        for b in range(4):
            for c in range(4):
                dp[i+1][0][a][b] = (dp[i+1][0][a][b] + dp[i][a][b][c]) % mod
                dp[i+1][3][a][b] = (dp[i+1][3][a][b] + dp[i][a][b][c]) % mod
                if a != 2 or b != 0:
                    dp[i+1][1][a][b] = (dp[i+1][1][a][b] + dp[i][a][b][c]) % mod
                if a == 1 and b == 0:
                    pass
                elif a == 0 and b == 1:
                    pass
                elif b == 1 and c == 0:
                    pass
                elif a == 1 and c == 0:
                    pass
                else:
                    dp[i+1][2][a][b] = (dp[i+1][2][a][b] + dp[i][a][b][c]) % mod

ans = 0
for a in range(4):
    for b in range(4):
        for c in range(4):
            ans = (ans + dp[-1][a][b][c]) % mod
print(ans)
