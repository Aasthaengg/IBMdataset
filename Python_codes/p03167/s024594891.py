

INF = float('inf')
M = 10 ** 9 + 7


def tc():
    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]

    dp = [[0] * w for _ in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#':
                continue
            if i > 0:
                dp[i][j] = (dp[i][j] + dp[i - 1][j]) % M
            if j > 0:
                dp[i][j] = (dp[i][j] + dp[i][j - 1]) % M

    print(dp[h - 1][w - 1])


tc()
