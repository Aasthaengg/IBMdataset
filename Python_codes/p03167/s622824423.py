n,m=map(int,input().split())

grid=[]
for i in range(n):
  x=list(input())
  grid.append(x)
  

dp=[[0 for i in range(m)] for j in range(n)]
dp[0][0]=1
for i in range(n):
  for j in range(m):
    if grid[i][j]!='#':
      if i>0:
        dp[i][j]+=dp[i-1][j]
      if j>0:
        dp[i][j]+=dp[i][j-1]
        
print(dp[n-1][m-1]%(10**9+7))        