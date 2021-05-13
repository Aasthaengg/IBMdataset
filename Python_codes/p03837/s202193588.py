import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]

import numpy as np
from scipy.sparse import *

N, M = ri_()
a = [0] * M
b = [0] * M
c = [0] * M
for i in range(M):
    ai, bi, ci = ri_()
    a[i], b[i], c[i] = ai - 1, bi - 1, ci
G = csr_matrix((c, (a, b)), shape=(N, N))
d = csgraph.floyd_warshall(G, directed=False)
ans = 0
for i in range(M):
    if d[a[i], b[i]] != c[i]:
        ans += 1
print(ans)