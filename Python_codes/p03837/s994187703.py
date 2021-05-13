from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

n, m = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(m)]

graph = [[0] * n for _ in range(n)]
for a, b, c in abc:
    a -= 1
    b -= 1
    graph[a][b] = c
    graph[b][a] = c

dist = floyd_warshall(csr_matrix(graph))

ans = 0
for a, b, c in abc:
    a -= 1
    b -= 1

    if dist[a][b] != c:
        ans += 1

print(ans)
