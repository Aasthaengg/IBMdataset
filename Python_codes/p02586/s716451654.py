
R, C, K = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(K)]

items = [[0] * (C + 1) for _ in range(R + 1)]
for r, c, v in X:
    items[r][c] = v

dp = [[0] * 4 for _ in range(C + 1)]
for i in range(1, R + 1):
    # Vertical transition
    for j in range(1, C + 1):
        dp[j][0] = max(dp[j])
        for k in range(1, 4):
            dp[j][k] = 0

    # Horizontal or picking-up transition
    for j in range(1, C + 1):
        for k in reversed(range(4)):
            dp[j][k] = max(dp[j][k], dp[j - 1][k])
            if items[i][j] and k < 3:
                dp[j][k + 1] = max(dp[j][k + 1], dp[j][k] + items[i][j])

print(max(dp[-1]))
