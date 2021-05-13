import sys
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
read = sys.stdin.read

N, M, *abc = map(int, read().split())
a, b, c = zip(*zip(*[iter(abc)] * 3))

graph = csr_matrix((c, (a, b)), shape=(N + 1, N + 1))
distance = dijkstra(graph, directed=False)

answer = 0

for i, j, k in zip(a, b, c):
    k = float(k)
    if k == distance[i][j]:
        continue

    for s in range(1, N + 1):
        if i == s or j == s:
            continue

        if k + distance[j][s] == distance[i][s]:
            break

        if k + distance[i][s] == distance[j][s]:
            break

    else:
        answer += 1

print(answer)