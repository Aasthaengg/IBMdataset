import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    P = [int(input()) for _ in range(N)]

    dp = [0] * (N + 1)

    for p in P:
        dp[p] = dp[p - 1] + 1

    print(N - max(dp))


if __name__ == '__main__':
    main()
