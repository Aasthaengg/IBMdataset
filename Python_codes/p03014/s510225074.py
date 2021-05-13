import sys

import numba as nb
import numpy as np

input = sys.stdin.readline


@nb.njit("i8(i8,i8,b1[:,:])", cache=True)
def solve(H, W, S):
    U = np.full(shape=(H + 2, W + 2), fill_value=-1, dtype=np.int64)
    D = np.full(shape=(H + 2, W + 2), fill_value=-1, dtype=np.int64)
    L = np.full(shape=(H + 2, W + 2), fill_value=-1, dtype=np.int64)
    R = np.full(shape=(H + 2, W + 2), fill_value=-1, dtype=np.int64)
    for h in range(1, H + 1):
        for w in range(1, W + 1):
            if not S[h][w]:
                continue
            if U[h][w] == -1:
                U[h][w] = 0
                d = 0
                while True:
                    d += 1
                    if not S[h + d][w]:
                        break
                    U[h + d][w] = d
            if L[h][w] == -1:
                L[h][w] = 0
                d = 0
                while True:
                    d += 1
                    if not S[h][w + d]:
                        break
                    L[h][w + d] = d

    for h in range(H + 1, 0, -1):
        for w in range(W + 1, 0, -1):
            if not S[h][w]:
                continue
            if D[h][w] == -1:
                D[h][w] = 0
                d = 0
                while True:
                    d += 1
                    if not S[h - d][w]:
                        break
                    D[h - d][w] = d
            if R[h][w] == -1:
                R[h][w] = 0
                d = 0
                while True:
                    d += 1
                    if not S[h][w - d]:
                        break
                    R[h][w - d] = d

    dist = U + D + L + R + 1
    ans = np.max(dist)
    return ans


def main():
    H, W = map(int, input().split())
    S = np.zeros(shape=(H + 2, W + 2), dtype=np.bool)
    for i in range(1, H + 1):
        S[i][1:-1] = [s == "." for s in input().rstrip()]

    ans = solve(H, W, S)

    print(ans)


if __name__ == "__main__":
    main()
