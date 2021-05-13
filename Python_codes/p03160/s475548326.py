n = int(input())
h = [None] + list(map(int, input().split()))

dp = [None for _ in range(n+1)]
for k in range(1,n+1):
  if k == 1:
    dp[k] = 0
  elif k == 2:
    dp[k] = abs(h[2] - h[1])
  else:
    dp[k] = min(
      dp[k-1] + abs(h[k] - h[k-1]),
      dp[k-2] + abs(h[k] - h[k-2])
    )
print(dp[k])