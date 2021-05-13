import sys

import numba as nb
import numpy as np

input = sys.stdin.readline


@nb.njit("i8(i8,i8[:],i8[:])", cache=True)
def binary_search(K, A, F):
    ng = -1
    ok = 10 ** 18
    while ok - ng > 1:
        mid = (ok + ng) // 2
        need_k = 0
        for a, f in zip(A, F):
            need_k += max(0, a - mid // f)
        if need_k <= K:
            ok = mid
        else:
            ng = mid
    return ok


def main():
    N, K = map(int, input().split())
    A = np.array(input().split(), dtype=np.int64)
    F = np.array(input().split(), dtype=np.int64)

    A = np.sort(A)
    F = np.sort(F)[::-1]

    ans = binary_search(K, A, F)
    print(ans)


if __name__ == "__main__":
    main()
