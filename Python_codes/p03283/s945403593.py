n, m, q = map(int, input().split())
lr = []
for _ in range(m):
    l, r = map(int, input().split())
    lr.append((l, r))
query = []
for _ in range(q):
    p, q = map(int, input().split())
    query.append((p, q))
accu = [[0]*(n+1) for _ in range(n+1)]
for l, r in lr:
    accu[l][r] += 1
for i in range(n):
    for j in range(n):
        accu[i+1][j+1] += accu[i+1][j]
for j in range(n):
    for i in range(n):
        accu[i+1][j+1] += accu[i][j+1]
ans = []
for p, q in query:
    ans.append(accu[q][q]-accu[q][p-1]-accu[p-1][q]+accu[p-1][p-1])
print(*ans, sep='\n')