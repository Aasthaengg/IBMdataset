N,M,R = map(int,input().split())
r = list(map(int,input().split()))
r.sort()
G = [[10**9 for i in range(N+1)] for j in range(N+1)]
for i in range(M):
    a,b,c = map(int,input().split())
    G[a][b] = min(G[a][b],c)
    G[b][a] = G[a][b]
def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d
warshall_floyd(G)
import itertools
ans = 10**9
for v in itertools.permutations(r):
    v = list(v)
    a = 0
    s = v.pop(0)
    for i in range(R-1):
        t = v[i]
        a += G[s][t]
        s = t
    ans = min(a,ans)
print(ans)
