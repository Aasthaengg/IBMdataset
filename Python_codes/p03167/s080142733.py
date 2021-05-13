H,W=map(int,input().split())
mod=10**9+7
grid=[]
for i in range(H):
    s=str(input())
    grid.append(s)
dp=[[0 for i in range(W)]for j in range(H)]
dp[0][0]=1
for i in range(H):
    for j in range(W):
        if (i+1 < H) and (grid[i+1][j]=="."):
            dp[i+1][j]+=dp[i][j]
        if (j+1 < W) and (grid[i][j+1]=="."):
            dp[i][j+1]+=dp[i][j]
print(dp[-1][-1]%mod)
