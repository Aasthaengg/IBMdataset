import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

n, m = map(int, input().split())
data = [1 for i in range(m)]
a = []
b = []

for i in range(m):
  _a, _b = map(int, input().split())
  a.append(_a - 1)
  b.append(_b - 1)

csr = csr_matrix((data, (a, b)), (n, n))

print(connected_components(csr, return_labels=False) - 1)