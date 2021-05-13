cap, m = map(int, input().split())
arr = list(map(int, input().split()))

INF = 1 << 60
dp = [INF] * (cap + 1)
dp[0] = 0

for x in arr:
    for i in range(x, cap + 1):
        dp[i] = min(dp[i], dp[i - x] + 1)

print(dp[cap])
