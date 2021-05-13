n, m = [int(x) for x in input().split()]
c = [0] + [int(x) for x in input().split()]
INF = float('inf')
dp = [[0] + [INF for _ in range(n)] for _ in range(2)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if j < c[i]:  # c[i]は使えない
            dp[i % 2][j] = dp[(i - 1) % 2][j]
        else:
            dp[i % 2][j] = min(dp[(i - 1) % 2][j], dp[i % 2][j - c[i]] + 1)

print(dp[m % 2][n])
