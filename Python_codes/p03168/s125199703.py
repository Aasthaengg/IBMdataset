N=int(input())
*p, = map(float,input().split())

dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
  if i == 1:
    dp[i][0] = 1-p[0]
    dp[i][1] = p[0]
    continue
  for j in range(i+1):
    if j == 0:
      dp[i][j] = dp[i-1][j]*(1-p[i-1])
      continue
    dp[i][j] = dp[i-1][j]*(1-p[i-1]) + dp[i-1][j-1]*p[i-1]
    
ans=0
for j in range(N//2+1,N+1):
  ans += dp[-1][j]
  
print(ans)