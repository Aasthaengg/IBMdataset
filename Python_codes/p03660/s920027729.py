import sys
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
read = sys.stdin.read

N, *ab = map(int, read().split())
a, b = zip(*zip(*[iter(ab)] * 2))

graph = csr_matrix(([1] * (N - 1), (a, b)), shape=(N + 1, N + 1))
distance = dijkstra(graph, directed=False, indices=[1, N])
d1 = distance[0]
dn = distance[1]

Fennec = -1
for i, j in zip(d1, dn):
    if i <= j:
        Fennec += 1

if Fennec > N - Fennec:
    print('Fennec')
else:
    print('Snuke')