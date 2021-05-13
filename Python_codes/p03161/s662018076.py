n, k = map(int, input().strip().split())
hs = list(map(int, input().strip().split()))

dp = [0] * n

for i in range(1, n):
    costs = []
    for j in range(1, k + 1):
        if i - j >= 0:
            cost = dp[i - j] + abs(hs[i] - hs[i - j])
            costs.append(cost)
    dp[i] = min(costs)

print(dp[n - 1])
