n = int(input())
dp = [0] * (2 * n + 1)
dp[n] = 1
for p in map(float, input().split()):
    ndp = [0] * (2 * n + 1)
    for i in range(1, 2 * n):
        ndp[i-1] += dp[i] * (1 - p)
        ndp[i+1] += dp[i] * p
    dp = ndp
print(sum(dp[n+1:]))