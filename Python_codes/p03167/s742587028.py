import sys

sys.setrecursionlimit(10 ** 9)


# map(int, sys.stdin.read().split())


def input():
    return sys.stdin.readline().rstrip()


def main():
    mod = 10 ** 9 + 7
    H, W = map(int, input().split())
    A = [[] for _ in range(H)]
    for i in range(H):
        A[i] = list(input())

    dp = [[0] * W] * H
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue
            if A[i][j] == "#":
                dp[i][j] = 0
                continue
            if i == 0:
                dp[i][j] = dp[i][j - 1]
            elif j == 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) %mod

    print(dp[H-1][W-1])

    pass


if __name__ == "__main__":
    main()
