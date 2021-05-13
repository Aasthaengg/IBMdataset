n = int(input())
a = [(int(j), i) for i, j in enumerate(input().split())]
a.sort(reverse=1)
dp = [[0] * (n+1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i + 1):
        k = i - j
        if j != 0:
            dp[i][j] = dp[i - 1][j - 1] + a[i-1][0] * (abs(j - 1 - a[i-1][1]))
        if k != 0:
            dp[i][j] = max(dp[i][j],
                           dp[i - 1][j] + a[i-1][0] * (abs(n-k - a[i-1][1])))
print(max(dp[-1]))