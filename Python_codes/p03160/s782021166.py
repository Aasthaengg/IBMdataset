N = int(input())
h = list(map(int, input().split()))

dp = [0]

for i in range(1, N):
    m = dp[i - 1] + abs(h[i] - h[i - 1])
    if i > 1:
        m = min(m, dp[i - 2] + abs(h[i] - h[i - 2]))
    dp.append(m)

print(dp[-1])