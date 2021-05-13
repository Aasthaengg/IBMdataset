def list2d(a, b, c): return [[c] * b for i in range(a)]
mod =10**9+7

n = int(input())
p = list(map(float, input().split()))
dp = list2d(n + 1,n + 1 ,0)

dp[0][0] = 1.
for i in range(1, n + 1):
  for j in range(n + 1):
    if(j==0):
      dp[i][j] = (1 - p[i-1])*dp[i-1][0]
    else:
      dp[i][j] = (1 - p[i-1])*dp[i-1][j] + p[i-1]*dp[i-1][j-1]
ans = 0
for k in range(n//2 + 1, n + 1):
  ans+=dp[n][k]
print(ans)
  
