from scipy.sparse.csgraph import dijkstra
import numpy as np

H, W = map(int, input().split())
C = [list(map(int, input().split())) for i in range(10)]
cost = np.r_[dijkstra(C)[:, 1], 0].astype(int)

A = np.array([list(map(int, input().split())) for i in range(H)])
print(cost[A].sum())