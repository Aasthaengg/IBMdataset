# coding: utf-8
import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# N**2の解法
N, M, Qu = lr()
graph = [[0] * (N+1) for _ in range(N+1)]  # 1-indexed
for i in range(M):
    l, r = lr()
    graph[l][r] += 1

graph = np.array(graph)
np.cumsum(graph, axis=1, out=graph)
np.cumsum(graph, axis=0, out=graph)
P = []; Q = []
for _ in range(Qu):
    p, q = lr()
    P.append(p); Q.append(q)

P = np.array(P); Q = np.array(Q)
answer = graph[Q, Q] - graph[Q, P-1] - graph[P-1, Q] + graph[P-1, P-1]
print('\n'.join(answer.astype(str)))
