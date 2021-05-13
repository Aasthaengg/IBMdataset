INF = 10**9

N, M = map(int, input().split())
key = [[]]
for i in range(M):
    a, b = map(int, input().split())
    C = list(map(int, input().split()))
    tmp = 0
    for c in C:
        tmp += 2**(c-1)
    key.append([a, tmp])

dp = [[INF for _ in range(2**N)] for _ in range(M+2)]
for i in range(1, M+1):
    dp[i][key[i][1]] = min(dp[i][key[i][1]], key[i][0])
    for j in range(2**N):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        dp[i][j|key[i][1]] = min(dp[i][j|key[i][1]], dp[i-1][j]+key[i][0])
if dp[M][2**N-1] == INF:
    print(-1)
else:
    print(dp[M][2**N-1])