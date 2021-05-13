n,ma,mb=map(int,input().split())
INF=10**17
dp=[[[INF]*(10*n+1) for i in range(10*n+1)] for j in range(n+1)]
dp[0][0][0]=0
ans=10**17
for i in range(n):
  a,b,c=map(int,input().split())
  for j in range(10*n+1):
    for k in range(10*n+1):
      if dp[i][j][k]!=INF:
        dp[i+1][j+a][k+b]=min(dp[i+1][j+a][k+b],dp[i][j][k]+c)
      dp[i+1][j][k]=min(dp[i+1][j][k],dp[i][j][k])
for i in range(1,10*n+1):
  for j in range(1,10*n+1):
    if i*mb==j*ma:
      ans=min(ans,dp[n][i][j])
if ans==INF:
  print(-1)
else:
  print(ans)