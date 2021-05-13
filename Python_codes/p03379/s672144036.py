import sys
input = sys.stdin.readline
import numpy as np
from numba import njit


def read():
    N = int(input().strip())
    X = np.fromstring(input().strip(), dtype=np.int32, sep=" ")
    return N, X


@njit
def solve(N, X):
    A = np.argsort(X)
    l, r = X[A[N//2-1]], X[A[N//2]]
    mid = (l + r) / 2
    for i in range(N):
        if X[i] <= mid:
            print(r)
        else:
            print(l)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
