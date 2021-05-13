# 解説AC
N = int(input())
A = map(int, input().split())

children = [(a, i) for i, a in enumerate(A)]

children.sort(reverse=True)

# dp[i][j]: うれしさの合計の最大値
# i: 左端の個数
# j: 右端の個数
dp = [[0] * (N + 1) for _ in range(N + 1)]

ans = 0
# 配るDP
for l in range(N):
    for r in range(N):
        if l + r == N:
            ans = max(ans, dp[l][r])
            break
        activeness, idx = children[l + r]
        dp[l + 1][r] = max(dp[l + 1][r], dp[l][r] + abs(idx - l) * activeness)
        dp[l][r + 1] = max(dp[l][r + 1], dp[l][r] + abs(idx - (N - 1 - r)) * activeness)

print(ans)