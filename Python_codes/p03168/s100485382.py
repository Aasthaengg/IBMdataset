

INF = float('inf')


def tc():
    n = int(input())
    p = list(map(float, input().split()))

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    # dp[i][j]: probability that out of the first
    # i coins, j of them are heads
    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] * (1 - p[i - 1])
        for j in range(1, i + 1):
            dp[i][j] = dp[i - 1][j] * (1 - p[i - 1]) + dp[i - 1][j - 1] * p[i - 1]

    ans = sum(dp[n][n // 2 + 1:])
    print(ans)


tc()
