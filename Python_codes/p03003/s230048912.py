n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
dp = [[0] * (m + 1) for _ in range(n + 1)]
sum = [[0] * (m + 1) for _ in range(n + 1)]
MOD = 10 ** 9 + 7

ans = 0
for i in range(n):
  for j in range(m):
    if s[i] == t[j]:
      dp[i + 1][j + 1] = (sum[i][j] + 1) % MOD
    else:
      dp[i + 1][j + 1] = 0
    sum[i + 1][j + 1] = (sum[i][j + 1] + sum[i + 1][j] 
                       - sum[i][j] + dp[i + 1][j + 1]) % MOD
    ans += dp[i + 1][j + 1]
    ans %= MOD
print((ans + 1) % MOD)
