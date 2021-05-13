import math

N = int(input())
h = list(map(int, input().split()))

dp = list([math.inf for i in range(N)])  # dpテーブル
dp[0] = 0
for i in range(N):
    a = dp[i]
    b = dp[i - 1] + abs(h[i] - h[i - 1])
    if a > b:
        dp[i] = b
    else:
        dp[i] = a
    a = dp[i]
    if i > 1:
        b2 = dp[i - 2] + abs(h[i] - h[i - 2])
        if a > b2:
            dp[i] = b2
        else:
            dp[i] = a

print(dp[N - 1])
