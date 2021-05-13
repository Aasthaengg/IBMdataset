import numpy as np
from numba import njit
N, K, *XY = [int(_) for _ in open(0).read().split()]
XY = np.array(XY, dtype=np.int64).reshape((N, 2)).T
X = np.sort(XY[0])
Y = np.sort(XY[1])

@njit
def solve(XY, X, Y):
    v = 4 * 10**18 + 1
    ans = np.array([0, 0, 0, 0], dtype=np.int64)
    for i1 in range(N - 1):
        x1=X[i1]
        for i2 in range(i1 + 1, N):
            x2=X[i2]
            for j1 in range(N - 1):
                y1=Y[j1]
                for j2 in range(j1 + 1, N):
                    y2 = Y[j2]
                    if np.sum((x1 <= XY[0]) * (XY[0] <= x2) * (y1 <= XY[1]) * (XY[1] <= y2)) < K:
                        continue
                    v2 = (x2 - x1) * (y2 - y1)
                    v = min(v, v2)
    return v

ans = solve(XY, X, Y)
print(ans)
