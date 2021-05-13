def calc():
  n,ma,mb=map(int,input().split())
  dp=[[[5000]*401 for _ in range(401)] for _ in range(41)]
  arr=[list(map(int,input().split())) for _ in range(n)]
  dp[0][0][0]=0
  for t in range(n):
    a,b,c=arr[t]
    for i in range(401):
      for j in range(401):
        if dp[t][i][j]==5000:
          continue
        dp[t+1][i][j]=min(dp[t+1][i][j],dp[t][i][j])
        dp[t+1][i+a][j+b]=min(dp[t+1][i+a][j+b],dp[t][i][j]+c)
  ans=5000
  for i in range(1,401):
    if i*ma>400 or i*mb>400:
      break
    ans=min(ans,dp[n][i*ma][i*mb])
  if ans==5000:
    print(-1)
  else:
    print(ans)
    
calc()