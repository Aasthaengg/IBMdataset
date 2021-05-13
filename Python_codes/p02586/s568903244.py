h,w,k=map(int,input().split())
dp=[[[0]*(w+2) for _ in range(h+2)] for _ in range(4)]
f=[[0]*(w+1) for _ in range(h+1)]
for _ in range(k):
  r,c,v=map(int,input().split())
  f[r][c]=v
for i in range(1,h+1):
  for j in range(1,w+1):
    for k in range(3,-1,-1):
      if k:dp[k][i][j]=max(dp[k][i][j],dp[k-1][i][j]+f[i][j])
      dp[0][i+1][j]=max(dp[0][i+1][j],dp[k][i][j])
      dp[k][i][j+1]=max(dp[k][i][j+1],dp[k][i][j])
print(max(dp[k][h][w] for k in range(4)))