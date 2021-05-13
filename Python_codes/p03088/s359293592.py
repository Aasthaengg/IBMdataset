mod=10**9+7
N=int(input())
dp=[[[[[0 for m in range(4)]for l in range(4)]for k in range(4)]for j in range(4)]for i in range(N+1)]
for i in range(4):
    for j in range(4):
        for k in range(4):
            dp[3][0][i][j][k]=1
dp[3][0][0][2][1]=0
dp[3][0][0][1][2]=0
dp[3][0][2][0][1]=0

for n in range(4,N+1):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                for a in range(4):
                    for i in range(4):
                        dp[n][b][c][d][a]+=dp[n-1][i][b][c][d]
                        dp[n][b][c][d][a]%=mod
                    dp[n][b][0][2][1]=0
                    dp[n][b][2][0][1]=0
                    dp[n][b][0][1][2]=0
                    dp[n][0][c][2][1]=0
                    dp[n][0][2][d][1]=0
ans=0
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                ans+=dp[N][a][b][c][d]
print(ans%mod)
#print(dp[3])