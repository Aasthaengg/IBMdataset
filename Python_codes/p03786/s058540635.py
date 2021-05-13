N = int(input())
A = list(map(int, input().split()))

import numpy as np

A = sorted(A)
B = np.cumsum(A)

mem = N
for i in range(N-1):
    if 2*B[i] >= A[i+1]:
        mem = min(i, mem)
    else:
        mem = N
print(N-mem)