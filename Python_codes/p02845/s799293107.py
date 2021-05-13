import copy
n = int(input())
a = list(map(int,input().split()))
dp = [[0,0,0] for _ in range(n+1)]
mod = 10**9+7
ans = 1
for i in range(1,n+1):
  dp[i] = copy.copy(dp[i-1])
  for j in range(3):
    if dp[i-1][j] == a[i-1]:
      dp[i][j] += 1
      break
  dp[i].sort(reverse=True)
for i in range(n):
  ans = ans*dp[i].count(a[i])%mod
print(ans)