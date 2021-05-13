import copy
N, M = map(int, input().split())
K = []
for i in range(N):
    x, y, z = map(int, input().split())
    K.append([x, y, z])

ans = 0
for i in range(2**3):
    dp = [[-10**12] * (M + 1) for _ in range(N + 1)]
    for u in range(N):
        dp[u][0] = 0
    P = copy.deepcopy(K)
    for l in range(3):
        if ((i >> l) & 1):
            for t in range(N):
                P[t][l] *= -1
    for j in range(1, N+1):
        for k in range(1, M+1):
            if k <= j:
                dp[j][k] = max([dp[j-1][k], dp[j-1][k-1] + sum(P[j-1])])
            else:
                dp[j][k] = dp[j-1][k]
    ans = max(ans, dp[N][M])

print(ans)