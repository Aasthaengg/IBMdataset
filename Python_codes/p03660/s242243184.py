import sys
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
read = sys.stdin.read

N, *ab = map(int, read().split())
a, b = zip(*zip(*[iter(ab)] * 2))

graph = csr_matrix(([1] * (N - 1), (a, b)), shape=(N + 1, N + 1))
distance = dijkstra(graph, directed=False, indices=[1, N])
d1 = distance[0][1:]
dn = distance[1][1:]

Fennec = np.count_nonzero(d1 <= dn)

if Fennec > N - Fennec:
    print('Fennec')
else:
    print('Snuke')