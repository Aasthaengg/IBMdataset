import numpy as np


def solve(N, K, A):
    E = np.arange(0, N)
    for _ in range(K):
        B = np.zeros(N + 1, dtype=np.int64)
        np.add.at(B, np.maximum(0, E - A), 1)
        np.add.at(B, np.minimum(E + A + 1, N), -1)
        A = np.cumsum(B)[:-1]
        if np.all(A == N):
            return A
    return A


N, K = map(int, input().split())
A = np.array(input().split(), dtype=int)
print(' '.join(map(str, solve(N, K, A))))