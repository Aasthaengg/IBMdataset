import sys
input=sys.stdin.readline
H,W,K=map(int,input().split())
G=[[0]*W for i in range(H)]

for i in range(K):
    r,c,v=map(int,input().split())
    r,c=r-1,c-1
    G[r][c]=v

dp=[[[-1]*W for i in range(H)] for i in range(4)]

dp[0][0][0]=0
if G[0][0]!=0:
    dp[1][0][0]=G[0][0]

for i in range(H):
    for j in range(W):
        m=max(dp[k][i][j] for k in range(4))
        if i+1<H:
            dp[1][i+1][j]=max(dp[1][i+1][j],m+G[i+1][j])
            dp[0][i+1][j]=max(dp[0][i+1][j],m)
        if j+1<W:
                dp[0][i][j+1]=0
                dp[1][i][j+1]=max(dp[1][i][j+1],dp[1][i][j],dp[0][i][j]+G[i][j+1])
                dp[2][i][j+1]=max(dp[2][i][j+1],dp[2][i][j],dp[1][i][j]+G[i][j+1])
                dp[3][i][j+1]=max(dp[3][i][j+1],dp[3][i][j],dp[2][i][j]+G[i][j+1])
ans=max(dp[i][H-1][W-1] for i in range(4))
print(ans)