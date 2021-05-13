from itertools import permutations
INFTY = 10**8
N,M,R = map(int,input().split())
r = list(map(int,input().split()))
G = {i:[] for i in range(1,N+1)}
for _ in range(M):
    a,b,c = map(int,input().split())
    G[a].append((b,c))
    G[b].append((a,c))
dist = [[INFTY for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    dist[i][i] = 0
for i in range(1,N+1):
    for j,d in G[i]:
        dist[i][j] = d
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
dmin = 10**8
for x in permutations(range(R),R):
    d = 0
    for k in range(1,R):
        d += dist[r[x[k]]][r[x[k-1]]]
    dmin = min(dmin,d)
print(dmin)