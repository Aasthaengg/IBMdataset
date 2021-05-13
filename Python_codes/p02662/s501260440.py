import sys
input = sys.stdin.readline
import numpy as np
from numba import njit


def read():
    N, S = map(int, input().strip().split())
    A = np.fromstring(input().strip(), dtype=np.int32, sep=" ")
    return N, S, A


@njit
def solve(N, S, A, MOD=998244353):
    dp = np.zeros((S+1), dtype=np.int32)
    dp[0] = 1
    for i in range(N):
        for j in range(S, -1, -1):
            v = 2 * dp[j]
            if j - A[i] >= 0:
                v += dp[j-A[i]]
            dp[j] = v % MOD
    return dp[S]


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
