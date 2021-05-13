N,M = map(int, input().split())
ng = set()
for i in range(M):
  ng.add(int(input()))
  
dp = [0] * (N + 5)
dp[0] = 1

for i in range(N):
  if i + 1 not in ng:
    dp[i + 1] += dp[i]
    dp[i + 1] %= 1000000007
  if i + 2 not in ng:
    dp[i + 2] += dp[i]
    dp[i + 2] %= 1000000007

print(dp[N])