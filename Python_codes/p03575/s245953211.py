from scipy.sparse.csgraph import connected_components
from scipy.sparse import coo_matrix
import numpy as np

N,M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
I,J = zip(*edges)

g = coo_matrix(([1]*M, (I,J)), (N+1, N+1))
g = g.tolil()

ans = 0
for i,j in edges:
    g[i,j] = 0
    cnt, _ = connected_components(g, directed=False)
    g[i,j] = 1
    ans += (cnt > 2)
print(ans)