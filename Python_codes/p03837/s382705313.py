import sys
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
read = sys.stdin.read

N, M, *abc = map(int, read().split())
a, b, c = zip(*zip(*[iter(abc)] * 3))

graph = csr_matrix((c, (a, b)), shape=(N + 1, N + 1))
distance = dijkstra(graph, directed=False).astype(int)

answer = 0

for i, j, k in zip(a, b, c):
    if k != distance[i][j]:
        answer += 1

print(answer)