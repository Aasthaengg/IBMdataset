n, k = map(int, input().split())
a = list(map(int, input().split()))

l = 50

dp = [[-1] * 2 for _ in range(l + 1)]
dp[0][0] = 0

for i in range(l):
    mask = 1 << (l - i - 1)
    ones = 0
    for e in a:
        if e & mask:
            ones += 1

    cost0 = mask * ones
    cost1 = mask * (n - ones)

    if dp[i][1] != -1:
        dp[i+1][1] = max(dp[i+1][1], dp[i][1] + max(cost0, cost1))

    if dp[i][0] != -1:
        if k & mask:
            dp[i+1][1] = max(dp[i+1][1], dp[i][0] + cost0)

    if dp[i][0] != -1:
        if k & mask:
            dp[i+1][0] = max(dp[i+1][0], dp[i][0] + cost1)
        else:
            dp[i+1][0] = max(dp[i+1][0], dp[i][0] + cost0)

ans = max(dp[l][0], dp[l][1])
print(ans)
