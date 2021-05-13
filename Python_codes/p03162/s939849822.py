import numpy as np


def main():
    n = int(input())
    d = [list(map(int, input().split())) for i in range(n)]

    dp = np.zeros((n, 3), dtype='int')
    dp[0] = d[0]

    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][1] + d[i][0], dp[i - 1][2] + d[i][0])
        dp[i][1] = max(dp[i - 1][0] + d[i][1], dp[i - 1][2] + d[i][1])
        dp[i][2] = max(dp[i - 1][0] + d[i][2], dp[i - 1][1] + d[i][2])

    print(max(dp[-1]))
    return


if __name__ == '__main__':
    main()
