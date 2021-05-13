H,W=map(int,input().split())

grid=[]

m=10**9+7

for i in range(H):
    a= list(input())
    grid.append(a)

dp=[ [0]*(W+3) for _ in range(H+3)]

for i in reversed(range(H)):
    for j in reversed(range(W)):
        dp[i][j] = dp[i+1][j] + dp[i][j+1]
        dp[H-1][W-1]=1
        if grid[i][j]=="#":
            dp[i][j]=0
print(dp[0][0]%m)