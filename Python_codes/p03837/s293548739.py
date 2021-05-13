import sys
input = sys.stdin.readline
read = sys.stdin.read

import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

n, m = map(int, input().split())
ABC = np.array(read().split(), dtype=np.int64).reshape(m, 3)
A, B, C = ABC.T
csr = csr_matrix((C, (A, B)), shape=(n+1, n+1))
F = floyd_warshall(csr, directed=False)
ans = 0
for a, b, c in ABC:
  if c != F[a, b]:
    ans += 1
print(ans)