N, W = map(int, input().split())
items = sorted([list(map(int, input().split())) for i in range(N)])

dp = [[0] * (W + 1) for i in range(N + 1)]

# dpテーブルを埋める
for i in range(N):
    wi, vi = items[i]
    for j in range(W + 1):
        if j + wi <= W:
            dp[i + 1][j + wi] = max(dp[i + 1][j + wi], dp[i][j] + vi)
        dp[i + 1][j] = max(dp[i][j], dp[i + 1][j])


ans = 0
# 最後に入れる商品は、残り容量１の時に入れるとしてしまってよい
for i, (wi, vi) in enumerate(items):
    ans = max(ans, dp[i][W - 1] + vi)

print(ans)