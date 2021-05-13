N = int(input())
MOD = 1000000007
dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
dp[0][3][3][3] = 1
for n in range(N):
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if (dp[n][i][j][k] == 0): continue
                for a in range(4):
                    if (j==0 and k==1 and a==2): continue
                    if (j==1 and k==0 and a==2): continue
                    if (j==0 and k==2 and a==1): continue
                    if (i==0 and k==1 and a==2): continue
                    if (i==0 and j==1 and a==2): continue
                    dp[n+1][j][k][a] += dp[n][i][j][k]
                    dp[n+1][j][k][a] %= MOD
ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            ans += dp[N][i][j][k]
            ans %= MOD
print(ans)
