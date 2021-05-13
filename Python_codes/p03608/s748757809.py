import itertools

n, m, r = map(int, input().split())
rs = list(map(int, input().split()))
rs = [r-1 for r in rs]

inf = float('inf')
dists = [[inf] * n for _ in range(n)]
for i in range(n):
    dists[i][i] = 0

for mm in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dists[a][b] = c
    dists[b][a] = c

## Warshall–Floyd
for k in range(n):
    for i in range(n):
        for j in range(n):
            dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])

tours = []
for perm in itertools.permutations(rs):
    d = 0
    for i in range(r-1):
        d += dists[perm[i]][perm[i+1]]
    tours.append(d)
print(min(tours))
    
