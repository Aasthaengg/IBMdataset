n, m, Q = map(int, input().split())

ts = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    l, r = tuple(map(int, input().split()))
    ts[l][r] += 1
# 二次元累積和
for i in range(1, n+1):
    for j in range(1, n+1):
        ts[i][j] += ts[i][j-1]

for i in range(1, n+1):
    for j in range(1, n+1):
        ts[i][j] += ts[i-1][j]

for _ in range(Q):
    p, q = tuple(map(int, input().split()))
    print(ts[q][q] - ts[p-1][q] - ts[q][p-1] + ts[p-1][p-1])

