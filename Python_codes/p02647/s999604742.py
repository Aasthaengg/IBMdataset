import numpy as np
from numba import njit


@njit('i8[:](i8,i8,i8[:])')
def solve(N, K, A):
    E = np.arange(0, N)
    for _ in range(K):
        B = np.zeros(N + 1, dtype=np.int64)
        for i_l, i_r in zip(np.maximum(0, E - A), np.minimum(E + A + 1, N)):
            B[i_l] += 1
            B[i_r] -= 1
        A = np.cumsum(B)[:-1]
        if np.all(A == N):
            return A
    return A


N, K = map(int, input().split())
A = np.array(input().split(), dtype=int)
print(' '.join(map(str, solve(N, K, A))))