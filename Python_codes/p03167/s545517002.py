r,c=map(int,input().split())
mod=10**9+7
g=[]
for _ in range(r):
  g.append(input())
dp=[[0 for j in range(c)] for i in range(r)]
dp[0][0]=1
for i in range(r):
  for j in range(c):
    if g[i][j]=='.':
        if i>0:
            dp[i][j]+=dp[i-1][j]%mod
        if j>0:
            dp[i][j]+=dp[i][j-1]%mod


print(dp[-1][-1]%mod)
      
