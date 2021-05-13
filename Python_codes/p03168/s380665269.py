#!python3

import numpy as np

LI = lambda: list(map(float, input().split()))

# input
N = int(input())
P = LI()


def main():
    dp = np.zeros((N + 1, N + 1))
    dp[0][0] = 1
    for i in range(1, N + 1):
        p = P[i - 1]
        bac = dp[i - 1][:i] * (1 - p)
        hos = dp[i - 1][:i] * p
        dp[i][:i] += bac
        dp[i][1 : i + 1] += hos
    ans = sum(dp[N][(N + 1) // 2:])
    print(ans)


if __name__ == "__main__":
    main()
