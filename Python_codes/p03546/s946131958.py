import numpy as np
H, W = (int(x) for x in input().split())
C = np.array([[int(x) for x in input().split()] for _ in range(10)])
A = [[int(x) if int(x) >= 0 else 1 for x in input().split()] for _ in range(H)]
from scipy.sparse.csgraph import dijkstra
C = dijkstra(C,directed=True) #有向グラフの経路圧縮（ダイクストラ法）
ans = sum(sum(C[x,1] for x in A))
print(int(ans))