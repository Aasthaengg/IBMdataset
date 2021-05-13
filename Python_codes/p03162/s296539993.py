import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    dp = [[0] * 3 for _ in range(N + 1)]

    for i in range(1, N + 1):
        dp[i] = list(map(int, input().split()))
        dp[i][0] += max(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] += max(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] += max(dp[i - 1][0], dp[i - 1][1])
    print(max(dp[N]))


if __name__ == "__main__":
    main()
