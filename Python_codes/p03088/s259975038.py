p = 10**9+7
N = int(input())
dp = [[[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
for j in range(4):
    for k in range(4):
        for l in range(4):
            if not(j==0 and k==1 and l==2) and not(j==0 and k==2 and l==1) and not(j==1 and k==0 and l==2):
                dp[3][0][j][k][l] = 1
for n in range(4,N+1):
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if not(j==0 and k==1 and l==2) and not(j==0 and k==2 and l==1) and not(j==1 and k==0 and l==2) \
                    and not(i==0 and k==1 and l==2) and not(i==0 and j==1 and l==2):
                        dp[n][i][j][k][l] = 0
                        for m in range(4):
                            dp[n][i][j][k][l] = (dp[n][i][j][k][l]+dp[n-1][m][i][j][k])%p
tot = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                tot = (tot + dp[N][i][j][k][l])%p
print(tot)