N = int(input())
MOD = 10**9 + 7
C = [int(input()) for i in range(N)]

dp = [0] * (N+1)
dp[0] = 1
last_idx = {}
for i, c in enumerate(C, 1):
  dp[i] = dp[i-1]
  if c in last_idx:
    idx = last_idx[c]
    if idx != i - 1:
      dp[i] += dp[idx]
      dp[i] %= MOD
  last_idx[c] = i

print(dp[-1]%MOD)