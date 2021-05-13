H, N = map(int, input().split())
INF = 10**9
dp= [INF for _ in range(H+1)]

dp[0] = 0

for i in range(N):
  a, b = map(int, input().split())
  for j in range(H):
    if j+a > H:
      dp[H] = min(dp[H], dp[j] + b)
    else:
      dp[j+a] = min(dp[j+a], dp[j] + b)
print(dp[H])