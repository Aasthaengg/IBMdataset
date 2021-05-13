# coding: utf-8
import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# N**2の解法
N, M, Q = lr()
graph = np.array([[0] * (N+1) for _ in range(N+1)])  # 1-indexed
for i in range(M):
    l, r = lr()
    graph[l][r] += 1

for i in range(N+1):
    graph[i] = graph[i].cumsum()

graph = np.cumsum(graph, axis=0)
for _ in range(Q):
    p, q = lr()
    answer = graph[q][q] - graph[q][p-1] - graph[p-1][q] + graph[p-1][p-1]
    print(answer)

# 30
