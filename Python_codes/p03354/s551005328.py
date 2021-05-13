import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

int1 = lambda x: int(x) - 1

N, M = map(int, input().split())
P = tuple(map(int1, input().split()))

edge = np.array([tuple(map(int1, input().split())) for _ in range(M)]).T
matr = csr_matrix((np.ones(M, dtype="int64"), edge), (N, N))

C, labels = connected_components(matr)
lst = [[set(), set()] for _ in range(C)]
for i, x in enumerate(labels):
    lst[x][0].add(i)
    lst[x][1].add(P[i])

for c in range(C):
    lst[c] = lst[c][0] & lst[c][1]
print(sum(len(s) for s in lst))