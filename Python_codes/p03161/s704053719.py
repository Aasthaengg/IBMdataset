import sys

import numpy as np

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    h = np.array(input().split(), dtype=np.int64)

    dp = np.zeros(shape=N, dtype=np.int64)
    dp[1] = abs(h[1] - h[0])
    for i in range(2, N):
        i_m = max(0, i - K)
        dp[i] = (dp[i_m:i] + np.abs(h[i] - h[i_m:i])).min()

    ans = dp[-1]
    print(ans)


if __name__ == "__main__":
    main()
