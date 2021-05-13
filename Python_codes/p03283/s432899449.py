n, m, q = map(int, input().split())
edges = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    L, R = map(int, input().split())
    edges[L][R] += 1

for i in range(1, n+1):
    for j in range(n):
        edges[i][j+1] += edges[i][j]

for i in range(n):
    for j in range(1, n+1):
        edges[i+1][j] += edges[i][j]

for _ in range(q):
    p, q = map(int, input().split())
    ans = edges[q][q]-edges[q][p-1]-edges[p-1][q]+edges[p-1][p-1]
    print(ans)
