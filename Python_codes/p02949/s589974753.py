import sys
import numpy as np
from scipy.sparse.csgraph import bellman_ford, connected_components
from scipy.sparse.csgraph._shortest_path import NegativeCycleError

input = sys.stdin.buffer.readline
epsilon = 2 ** -26 # > 10 ** -8, which is the smallest cost scipy's bellman_ford can deal with. 

N, M, P = map(int, input().split())
graph = np.zeros((N, N), np.float64)
for _ in range(M):
    a, b, c = map(int, input().split())
    if graph[a-1][b-1] == 0:
        if -c+P == 0:
            graph[a-1][b-1] = epsilon
        else:
            graph[a-1][b-1] = -c+P
    elif graph[a-1][b-1] > -c+P:
        if -c+P == 0:
            graph[a-1][b-1] = epsilon
        else:
            graph[a-1][b-1] = -c+P

tmp = graph[-1, 0]
#connect N to 1
graph[-1, 0] = epsilon
_, labels = connected_components(graph, connection = "strong")
mask = (labels == labels[0])

#recover original N to 1 path.
graph[-1, 0] = tmp
graph = graph[mask, :][:, mask]

try:
    ans = bellman_ford(graph, directed = True, indices = 0)[-1]
    ans = max(0, int(round(-ans)))
except NegativeCycleError:
    ans = -1

print(ans)
