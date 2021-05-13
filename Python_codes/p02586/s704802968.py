import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    R, C, K = map(int, input().split())

    field = [[0 for j in range(C)] for i in range(R)]

    for _ in range(K):
        r, c, v = map(int, input().split())
        field[r - 1][c - 1] += v

    dp = [[0] * 4 for j in range(C)]

    for i in range(R):
        for j in range(C):
            ct = field[i][j]
            premax = max(dp[j])

            if ct == 0:
                if j>0:
                    dp[j][0] = max(dp[j - 1][0], premax)
                else:
                    dp[j][0] = premax

                for k in range(1, 4):
                    if j > 0:
                        dp[j][k] = dp[j - 1][k]
            else:
                if j>0:
                    dp[j][0] = max(dp[j - 1][0], premax)
                    dp[j][1] = max(ct + max(dp[j - 1][0], premax), dp[j - 1][1])
                else:
                    dp[j][0] = premax
                    dp[j][1] = premax +ct
                for k in range(2, 4):
                    if j > 0:
                        dp[j][k] = max(dp[j - 1][k - 1] + ct, dp[j - 1][k])

    print(max(dp[C - 1]))


if __name__ == "__main__":
    main()
