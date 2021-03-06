import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N, M = map(int, input().split())

    dp = [INF for i in range(1 << N)]
    dp[0] = 0

    key = []
    for _ in range(M):
        a, b = map(int, input().split())
        C = tuple(map(lambda x: int(x) - 1, input().split()))
        status = 0
        for c in C:
            status += 2 ** c
        key.append((a, status))

    for a, status in key:
        if dp[status] > a:
            dp[status] = a

    for i in range(2 ** N - 1):
        for a, status in key:
            new_status = status | i
            if dp[new_status] > dp[i] + a:
                dp[new_status] = dp[i] + a

    if dp[-1] == INF:
        print(-1)
    else:
        print(dp[-1])


if __name__ == "__main__":
    main()
