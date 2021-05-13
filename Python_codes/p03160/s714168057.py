N = int(input())
h = list(map(int, input().split()))

dp = [-1] * N

dp[0] = 0
dp[1] = dp[0] + abs(h[1] - h[0])

for x in range(2, N):
    dp[x] = min(dp[x - 1] + abs(h[x] - h[x - 1]),
                dp[x - 2] + abs(h[x] - h[x - 2]))
print(dp[N - 1])