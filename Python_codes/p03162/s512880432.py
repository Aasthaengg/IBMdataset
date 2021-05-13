import sys
from collections import deque
from operator import itemgetter


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    A = []
    B = []
    C = []
    for i in range(N):
        a, b, c = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    dp = [[0] * 3 for _ in range(N + 1)]
    for i in range(1, N + 1):
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + A[i - 1]
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + B[i - 1]
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + C[i - 1]
    print(max(dp[N]))


if __name__ == "__main__":
    main()
