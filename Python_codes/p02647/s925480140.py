import sys
import numpy as np
from numba import njit
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@njit('(i8[::1],)', cache=True)
def update(A):
    N = len(A)
    B = np.zeros_like(A)
    for i, x in enumerate(A):
        l = max(0, i - x)
        r = min(N - 1, i + x)
        B[l] += 1
        if r + 1 < N:
            B[r + 1] -= 1
    B = np.cumsum(B)
    return B

N, K = map(int, readline().split())
A = np.array(read().split(), np.int64)

K = min(K, 100)
for _ in range(K):
    A = update(A)
print(' '.join(A.astype(str)))
