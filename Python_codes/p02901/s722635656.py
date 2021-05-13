N, M = map(int, input().split())
a = [0]*M
b = [0]*M
c = [0]*M
for i in range(M):
    a[i], b[i] = map(int, input().split())
    cc = list(map(int, input().split()))
    for ccc in cc:
        ccc -= 1
        c[i] += (1 << ccc)

INF = float('inf')
dp = [[INF]*5000 for _ in range(M+1)]
dp[0][0] = 0

for i in range(M):
    for j in range((1 << N)):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        nj = j | c[i]
        dp[i+1][nj] = min(dp[i+1][nj], dp[i][j] + a[i])
if dp[M][(1 << N)-1] == INF:
    print(-1)
else:
    print(dp[M][(1 << N)-1])
