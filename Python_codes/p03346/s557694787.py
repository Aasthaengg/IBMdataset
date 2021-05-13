import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    P = [int(input()) for _ in range(N)]

    # dp[i] := i が一番右端に来るときの最大長
    dp = [0] * (N + 1)
    for i in range(N):
        p = P[i]
        dp[p] = dp[p - 1] + 1

    print(N - max(dp))


if __name__ == "__main__":
    main()
