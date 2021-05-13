import numpy as np
from numba import njit
INF = 10**12


@njit
def main(N, K, H):
    dp = [INF]*(N)
    dp[0] = 0
    for i in range(N):
        for s in range(K):
            if i-s-1 < 0:
                break
            dp[i] = min(dp[i], dp[i-s-1] + abs(H[i-s-1] - H[i]))
    print(dp[-1])


if __name__ == '__main__':
    N, K = (int(i) for i in input().split())
    H = np.array([int(i) for i in input().split()], dtype=np.int32)
    main(N, K, H)
