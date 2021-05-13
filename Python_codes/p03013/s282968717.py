N, M = [int(x) for x in input().split()]
a = set(int(input()) for _ in range(M))

MOD = 10 ** 9 + 7
dp = [0] * (N + 1)
dp[0] = 1

for i in range(1, N + 1):
  if i in a:
    continue
  x = dp[i - 1]
  if i > 1:
    x += dp[i - 2]
  dp[i] = x % MOD

ans = dp[N]
print(ans)