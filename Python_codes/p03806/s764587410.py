n,ma,mb=map(int,input().split())
INF=10**18
dp=[[[INF for _ in range(401)] for _ in range(401)] for _ in range(n+1)]
ce=[[] for _ in range(n)]
for i in range(n):
  ce[i]=tuple(map(int,input().split()))
dp[0][0][0]=0
for k in range(n):
  for i in range(401):
    for j in range(401):
      a,b,c=ce[k]
      dp[k+1][i][j]=min(dp[k+1][i][j],dp[k][i][j])
      if i+a<401 and j+b<401:
        dp[k+1][i+a][j+b]=min(dp[k+1][i+a][j+b],dp[k][i][j]+c)
ans=INF
for i in range(1,401):
  for j in range(1,401):
    if i*mb==j*ma:ans=min(ans,dp[n][i][j])
if ans==INF:ans=-1
print(ans)