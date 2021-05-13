N, Ma, Mb = map(int, input().split())
l = []
for i in range(N):
    l.append(list(map(int, input().split())))
ans = float('inf')

Mab = 10 * N + 1
dp = [[[float('inf')] * Mab for _ in range(Mab)] for _ in range(N + 1)]
dp[0][0][0] = 0
for n in range(N):
    for a in range(10 * N):
        for b in range(10 * N):
            if dp[n][a][b] == float('inf'):
                continue
            dp[n + 1][a][b] = min(dp[n + 1][a][b], dp[n][a][b])
            dp[n + 1][a + l[n][0]][b + l[n][1]] = min(dp[n + 1][a + l[n][0]][b + l[n][1]], dp[n][a][b] + l[n][2])
# np.set_printoptions(threshold=np.inf)
# print(dp)
for a in range(1, 10 * N):
    for b in range(1, 10 * N):
        if a * Mb == b * Ma:
            ans = min(ans, dp[n + 1][a][b])
if ans == float('inf'):
    print(-1)
else:
    print(int(ans))
