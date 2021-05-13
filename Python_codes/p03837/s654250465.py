import sys
from scipy.sparse.csgraph import shortest_path
import numpy as np

stdin = sys.stdin

ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split())) # applies to numbers only
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

N, M = rl()
edges = [rl() for _ in range(M)]
graph = np.zeros((N, N))

for a, b, c in edges:
    graph[a-1, b-1] = c

dist = shortest_path(graph, directed=False).astype(int)
answer = 0
for a, b, c in edges:
    if c != dist[a-1, b-1]:
        answer += 1

print(answer)
#05