N, M = map(int, input().split())
Cost = []
for i in range(M):
    a, b = map(int, input().split())
    c = 0
    K = list(map(int, input().split()))
    for j in range(b):
        c += 2**(K[j]-1)
    Cost.append([c, a])

dp = [[float("inf")]*(2**N+1) for _ in range(M+1)]
for i in range(M+1):
    dp[i][0] = 0

for i in range(1, M+1):
    for j in range(2**N):
        k = Cost[i-1][0] | j
        dp[i][j] = min(dp[i-1][j], dp[i][j])
        dp[i][k] = min([dp[i-1][j] + Cost[i-1][1], dp[i-1][k], dp[i][k]])

if dp[M][2**N-1] == float("inf"):
    print(-1)
else:
    print(dp[M][2**N-1])
