n,ma,mb = map(int,input().split())
abc = [list(map(int,input().split())) for i in range(n)]
dp = [[[10000 for i in range(n*10+1)] for j in range(n*10+1)] for k in range(n+1)]
for i in range(n+1):
  dp[i][0][0] = 0
for i in range(1,n+1):
  x,y,c = abc[i-1]
  for j in range(1,n*10+1):
    for k in range(1,n*10+1):
      if j>=x and k>=y:
        dp[i][j][k] = min(dp[i][j][k],dp[i-1][j][k],dp[i-1][j-x][k-y]+c)
      else:
        dp[i][j][k] = min(dp[i][j][k],dp[i-1][j][k])
ans = 10000000
for i in range(1,n*10+1):
  for j in range(1,n*10+1):
    if i*mb == j*ma:
      ans = min(ans,dp[n][i][j])
if ans == 10000:
  print(-1)
else:
  print(ans)