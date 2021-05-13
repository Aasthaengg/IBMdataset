N, K = map(int, input().split())

A = [[] for _ in range(N)]
B = [[] for _ in range(N)]

for i in range(N):
    A[i], B[i] = map(int, input().split())

import numpy as np
Ind = np.argsort(A)

mem = K
for ind in Ind:
    mem -= B[ind]
    if mem <= 0:
        print(A[ind])
        break