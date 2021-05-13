import numpy as np  # noqa
import numba
from numba import njit, b1, i4, i8, f8

m = 998244353
N, K = map(int, input().split())

jumps = []
for i in range(K):
    l, r = map(int, input().split())
    jumps.append(l)
    jumps.append(r)


jumps = np.array(jumps)


@njit((i8, i8, i8[:]), cache=True)
def main(N, m, jumps):
    L, R = jumps[::2], jumps[1::2]
    dpsum = np.zeros(N + 1)
    dp = np.zeros(N + 1)
    dp[1] = dpsum[1] = 1

    for i in range(2, N + 1):
        for j in range(len(L)):
            mn = max(0, i - R[j])
            mx = max(mn, i - L[j])
            dp[i] = (dp[i] + dpsum[mx] - dpsum[mn - 1]) % m
        dpsum[i] = (dp[i] + dpsum[i - 1]) % m
    return dp[N]


print(int(main(N, m, jumps)))
