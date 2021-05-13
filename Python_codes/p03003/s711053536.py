import numpy as np
from numba import njit

MOD = 10 ** 9 + 7

N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

@njit
def solve(N, M, S, T):
    dp = np.ones((N+1, M+1), np.int64)
    for i, s in enumerate(S):
        for j, t in enumerate(T):
            dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1]
            if s != t:
                dp[i+1][j+1] -= dp[i][j]
            dp[i+1][j+1] %= MOD
    return dp[N][M]

print(solve(N, M, S, T))
