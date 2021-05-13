import numpy as np
from numba import njit, i8


@njit(i8(i8, i8, i8[:]), cache=True)
def solve(N, S, A):
    MOD = 998244353
    dp = np.zeros((N + 1, S + 1), dtype=np.int64)
    dp[0][0] = 1
    for i in range(N):
        for j in range(S + 1):
            dp[i + 1][j] += 2 * dp[i][j]
            dp[i + 1][j] %= MOD
            if j + A[i] <= S:
                dp[i + 1][j + A[i]] += dp[i][j]
                dp[i + 1][j + A[i]] %= MOD
    return dp[-1][-1]


N, S = map(int, input().split())
A = np.array(input().split(), dtype=np.int64)
print(solve(N, S, A))
