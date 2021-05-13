N, M = (int(s) for s in input().split())

broken = {int(input()) for _ in range(M)}

dp = [1 for _ in range(N+1)]

for k in range(1, N+1):
  if k in broken:
    dp[k] = 0
  elif k > 1:
    dp[k] = dp[k-1] + dp[k-2]

print(dp[N] % 1000000007)