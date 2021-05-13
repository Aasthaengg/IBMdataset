import sys
import numpy as np
import numba
from numba import njit
from numba.types import Omitted
i4 = numba.int32
i8 = numba.int64

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@njit((i8[:, :], i8), cache=True)
def main(S, K):
    H, W = S.shape
    ans = H + W + 100
    for s in range(1 << H - 1):
        cost = 0
        T = S.copy()
        for i in range(H - 1):
            if s & 1 << i:
                T[i + 1] += T[i]
            else:
                cost += 1
        if np.any(T > K):
            continue
        cumsum = np.zeros(H, np.int64)
        for w in range(W):
            if np.any(cumsum + T[:, w] > K):
                cumsum[:] = 0
                cost += 1
            cumsum += T[:, w]
        ans = min(ans, cost)
    return ans

H, W, K = map(int, readline().split())
S = np.empty((H, W), np.int64)
for h in range(H):
    S[h] = np.array(list(readline().rstrip().decode()))

print(main(S, K))