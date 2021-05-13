INF=10**18
H,W=map(int,input().split())
G=[list(input()) for i in range(H)]

dp=[[INF]*W for i in range(H)]
dp[0][0]=0
dx=[0,1]
dy=[1,0]

for i in range(H):
    for j in range(W):
        for x,y in zip(dx,dy):
            if i+x>=H or j+y>=W:
                continue
            if G[i][j]=='.' and G[i+x][j+y]=='#':
                dp[i+x][j+y]=min(dp[i][j]+1,dp[i+x][j+y])
            else:
                dp[i+x][j+y]=min(dp[i][j],dp[i+x][j+y])
ans=dp[H-1][W-1]
print(ans if G[0][0]!='#' else ans+1)