import sys
from scipy.sparse.csgraph import csgraph_from_dense
from scipy.sparse.csgraph import floyd_warshall
input = sys.stdin.readline


n, m, energy = map(int, input().split())
edges = [[float('INF')]*n for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    edges[a-1][b-1] = c
    edges[b-1][a-1] = c

G = csgraph_from_dense(edges, null_value=float('INF'))
dist = floyd_warshall(G, directed=False)

L_edges = [[0]*n for _ in range(n)]
for i in range(n-1):
    for j in range(i, n):
        if dist[i][j] <= energy:
            L_edges[i][j] = 1
            L_edges[j][i] = 1

G = csgraph_from_dense(L_edges, null_value=0)
answers = floyd_warshall(G, directed=False)

Q = int(input())
for i in range(Q):
    s, t = map(int, input().split())
    ans = answers[s-1][t-1] - 1
    if ans == float('INF'):
        print(-1)
    else:
        print(int(ans))
