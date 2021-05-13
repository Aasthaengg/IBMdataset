H, N = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]

INF = 10 ** 9
dp = [INF] * (H+1)
dp[0] = 0
for i in range(H):
    for j in range(N):
        idx = min(H, i+ab[j][0])
        dp[idx] = min(dp[idx], dp[i]+ab[j][1])
print(dp[-1])