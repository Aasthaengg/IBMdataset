import numpy as np
from scipy.sparse.csgraph import shortest_path
 
H, W, *t = map(int, open(0).read().split())
c = np.array(t[:100]).reshape((10, 10))
A = np.array(t[100:])
print(int(np.sum(shortest_path(c)[:, 1][A[A >= 0]])))