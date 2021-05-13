r,c,k=map(int, input().split())
grid=[[0]*(c+1) for _ in range(r+1)]
for i in range(k):
    ri,ci,vi=map(int, input().split())
    grid[ri][ci]=vi

dp=[[[0]*(c+1) for _ in range(r+1)] for _ in range(4)]

for i in range(1,r+1):
    for j in range(1,c+1):
        for k in range(4):
            dp[0][i][j]=max(dp[0][i][j],dp[k][i-1][j])
            dp[k][i][j]=max(dp[k][i][j],dp[k][i][j-1])
        if grid[i][j]!=0:
            dp[1][i][j]=max(dp[1][i][j],dp[0][i-1][j]+grid[i][j])
            for k in range(1,4):
                dp[1][i][j]=max(dp[1][i][j],dp[k][i-1][j]+grid[i][j])
                dp[k][i][j]=max(dp[k][i][j],dp[k-1][i][j-1]+grid[i][j])

ans=0
for k in range(4):
    ans=max(ans,dp[k][-1][-1])
print(ans)