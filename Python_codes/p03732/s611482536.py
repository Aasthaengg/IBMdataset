import collections

n, w = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(n)]

dp = [collections.defaultdict(lambda: 0) for _ in range(n + 1)]
dp[0][0] = 0
for i, (w0, v0) in enumerate(ls):
    for w1, v1 in dp[i].items():
        if w1 <= w:
            dp[i + 1][w1] = max(dp[i + 1][w1], v1)
        if w0 + w1 <= w:
            if w0 + w1 in dp[i].keys():
                dp[i + 1][w0 + w1] = max(dp[i + 1][w0 + w1], dp[i][w0 + w1],
                                         v0 + v1)
            else:
                dp[i + 1][w0 + w1] = v0 + v1
print(max(dp[n].values()))