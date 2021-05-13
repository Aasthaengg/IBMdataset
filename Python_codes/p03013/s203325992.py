n, m = map(int, input().split())
A = set([int(input()) for _ in range(m)])
MOD = 10 ** 9 + 7

dp = [0] * (n + 1)
dp[0] = 1

for i in range(n + 1):
  if i > 1:
    if i not in A:
      dp[i] += dp[i - 2]
  if i > 0:
    if i not in A:
      dp[i] += dp[i - 1]
  dp[i] %= MOD

print(dp[-1])