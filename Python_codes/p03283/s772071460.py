"""ABC106D AtCoder Express2 diff:1306
"""

N, M, Q = map(int, input().split())
x = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    L, R = map(int, input().split())
    x[L][R] += 1
cum = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        cum[i][j] = cum[i-1][j] + cum[i][j-1] - cum[i-1][j-1] + x[i][j]

for _ in range(Q):
    p, q = map(int, input().split())
    ans = cum[q][q] - cum[p-1][q] - cum[q][p-1] + cum[p-1][p-1]
    print(ans)
