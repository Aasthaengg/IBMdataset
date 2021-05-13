
N, M = map(int, input().split())
X = []
for i in range(M):
    a, _ = map(int, input().split())
    c = list(map(int, input().split()))
    key = sum(1 << (v - 1) for v in c)
    X.append([key, a])

INF = 10 ** 9 + 7
dp = [[INF] * (2 ** N) for _ in range(M + 1)]
dp[0][0] = 0
for i in range(M):
    for j in range(2 ** N):
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        dp[i + 1][j | X[i][0]] = min(dp[i + 1][j | X[i][0]],
                                     dp[i][j] + X[i][1])

if dp[-1][-1] == INF:
    print(-1)
else:
    print(dp[-1][-1])
