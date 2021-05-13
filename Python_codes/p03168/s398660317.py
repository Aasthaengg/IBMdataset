n = int(input())
p = list(map(float, input().split()))

dp = [1] * (n + 1)
dp2 = [1] * (n + 1)
dp[0] = 1 - p[0]
dp[1] = p[0]

for i in range(2, n + 1):
    dp2[0] = dp[0] * (1 - p[i - 1])
    dp2[i] = dp[i - 1] * p[i - 1]
    for j in range(1, i):
        dp2[j] = dp[j] * (1 - p[i - 1]) + dp[j - 1] * p[i - 1]
    for k in range(n + 1):
        dp[k] = dp2[k]
print(sum(dp[(n + 1) // 2:]))
