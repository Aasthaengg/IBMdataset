import sys
N, K = map(int, input().split())
h = [0] + list(map(int, input().split()))
dp = [0]*(N+1) # 足場iにたどり着くまでの最小コスト
for i in range(2,N+1):
  dp[i] = dp[i-1] + abs(h[i]-h[i-1])
  for j in range(1,K+1):
    if i-j > 0:
      dp[i] = min(dp[i],dp[i-j]+abs(h[i]-h[i-j]))
print(dp[-1])