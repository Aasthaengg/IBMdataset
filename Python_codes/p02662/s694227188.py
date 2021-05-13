#!/usr/bin/env python3
import sys
from functools import lru_cache
sys.setrecursionlimit(10**8)

MOD = 998244353  # type: int


def main():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    DP = [[0]*(S+1) for i in range(N+1)]
    DP[0][0] = 1
    for i in range(1, N+1):
        for wa in range(S+1):
            DP[i][wa] = 2*DP[i-1][wa]
            DP[i][wa] %= MOD
            if 0 <= wa-A[i-1] <= S:
                DP[i][wa] += DP[i-1][wa-A[i-1]]
                DP[i][wa] %= MOD

    print(DP[N][S])
    return


if __name__ == '__main__':
    main()
