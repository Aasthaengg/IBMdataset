md = 1000000007
n,m = map(int,input().split())

grid=[]
for i in range(n):
    grid.append(list(input()))

dp=[]
for i in range(n):
    dp.append([0]*m)
dp[0][0]=1
for i in range(1,n):
    if(grid[i][0]!="#"):
        dp[i][0]=dp[i-1][0]
    else:
        dp[i][0]=0

for j in range(1,m):
    if(grid[0][j]!="#"):
        dp[0][j]=dp[0][j-1]
    else:
        dp[0][j]=0

for i in range(1,n):
    for j in range(1,m):
        if(grid[i][j]=="#"):
            dp[i][j]=0
        else:
            dp[i][j]=(dp[i-1][j]+dp[i][j-1])%md
print(dp[n-1][m-1])
