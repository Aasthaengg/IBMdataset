import numpy as np
from scipy.sparse.csgraph import floyd_warshall

h, w = map(int, input().split())
graph = np.array([list(map(int, input().split())) for _ in range(10)])

cost = floyd_warshall(graph)
cost = cost.astype(int)

arr = np.array([list(map(int, input().split())) for _ in range(h)])
arr = arr.flatten()

ans = 0
for x in arr:
    if x == -1:
        continue
    else:
        ans += cost[x][1]

print(ans)