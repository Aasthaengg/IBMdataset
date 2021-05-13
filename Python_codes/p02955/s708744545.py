import numpy as np
import sys
# from numba import njit


def solve(A, K, div):
    for d in range(div.shape[0] - 1, 0, -1):
        res = div[d]
        B = np.sort(A % res)
        if B[B.shape[0] - 1] == 0:
            return res
        i = 0
        j = B.shape[0] - 1
        cost = res - B[j]
        scost = 0
        while j - i > 0:
            for n in range(i, j):
                scost += B[n]
                if scost >= cost:
                    while scost > cost:
                        j -= 1
                        cost += res - B[j]
                    i = n + 1
                    break
            else:
                i = j
        if K >= cost:
            return res
    return 1


def divisor(d, div):
    r = int(d ** 0.5 - 0.0000001) + 1
    ind = 0
    for i in range(1, r):
        if d % i == 0:
            div[ind] = i
            ind += 1
            div[ind] = d // i
            ind += 1
    if d % r == 0:
        div[ind] = r
        ind += 1
    return ind


line = sys.stdin.readline
N, K = map(int, line().split())
A = np.fromstring(line(), dtype=np.int64, sep=' ')
d = A.sum()
div = np.empty(10 ** 6, dtype=np.int64)
num = divisor(d, div)
div = np.sort(div[:num])
print(solve(A, K, div))
