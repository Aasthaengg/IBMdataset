INF = 10 ** 9
N, M = map(int,input().split())
dp = [[INF for i in range(1 << N)] for j in range(M+1)]
dp[0][0] = 0
for i in range(M):
    a, b = map(int,input().split())
    c = list(map(int,input().split()))
    k = 0
    for l in c:
        k += 1 << (l - 1)
    for j in range(1 << N):
        if dp[i][j] != INF:
            dp[i+1][j] = min(dp[i][j], dp[i+1][j])
            dp[i+1][j | k] = min(dp[i+1][j | k], dp[i][j] + a)

if dp[-1][-1] == INF:
    print(-1)
else:
    print(dp[-1][-1])