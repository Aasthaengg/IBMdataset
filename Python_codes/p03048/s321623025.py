r, g, b, n = map(int, input().split())

dp = [0 for i in range(n+1)]
dp[0] = 1

for i in range(r, n+1, r):
    dp[i] = 1
for i in range(g, n+1):
    dp[i] += dp[i-g]
for i in range(b, n+1):
    dp[i] += dp[i-b]

print(dp[-1])