N, M = [int(i) for i in input().split()]
UVm = [[int(i) for i in input().split()] for _ in range(M)]
S, T = [int(i) for i in input().split()]

graphs = [[] for _ in range( 3 * N)]
dists = [-1 for _ in range( 3 * N)]
for uv in UVm:
  u = uv[0] - 1
  v = uv[1] - 1
  graphs[u].append(v + N)
  graphs[u + N].append( v + 2 * N)
  graphs[u + 2 * N].append(v)
  
def dist(s, t, g):
    q = [s]
    dists = [-1]*len(g)
    dists[s] = 0
    while len(q) != 0:
        p = []
        for u in q:
            for v in g[u]:
                if dists[v] != -1:
                    continue
                p.append(v)
                dists[v] = dists[u] + 1
        q = p
    return dists[t]
print(dist(S-1, T-1, graphs)//3)

