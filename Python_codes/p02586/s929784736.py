f=lambda:map(int,input().split())
R,C,K=f()
g=[[0]*(C+1) for _ in range(R+1)]
for _ in range(K):
  r,c,v=f()
  g[r][c]=v
dp=[[[0]*(C+2) for _ in range(R+2)] for _ in range(4)]
for i in range(1,R+1):
  for j in range(1,C+1):
    for k in range(3,-1,-1):
      if k: dp[k][i][j]=max(dp[k][i][j],dp[k-1][i][j]+g[i][j])
      dp[0][i+1][j]=max(dp[0][i+1][j],dp[k][i][j])
      dp[k][i][j+1]=max(dp[k][i][j+1],dp[k][i][j])
print(max(dp[k][R][C] for k in range(4)))