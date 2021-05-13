import math

N = int(input())
h = list(map(int, input().split()))
h += [math.inf, math.inf]

dp = list([math.inf for i in range(N + 2)])  # dpテーブル
dp[0] = 0
for i in range(N):
    if dp[i + 1] > (dp[i] + abs(h[i] - h[i + 1])):
        dp[i + 1] = (dp[i] + abs(h[i] - h[i + 1]))
    else:
        dp[i + 1] = dp[i + 1]
    if dp[i + 2] > dp[i] + abs(h[i] - h[i + 2]):
        dp[i + 2] = dp[i] + abs(h[i] - h[i + 2])
    else:
        dp[i + 2] = dp[i + 2]

print(dp[N - 1])
