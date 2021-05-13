h, n = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]
inf = 1 << 30
dp = [inf] * (h + 1)
dp[h] = 0

for i in range(n):
    for j in range(h, 0, -1):
        nx = max(0, j - ab[i][0])
        dp[nx] = min(dp[nx], dp[j] + ab[i][1])
print(dp[0])