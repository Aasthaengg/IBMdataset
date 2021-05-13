import sys
from collections import deque
from operator import itemgetter


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    h.insert(0,0)
    dp = [10 ** 9 + 7] * (N + 1)
    dp[1] = 0
    for i in range(1, N + 1):
        for k in range(1, K + 1):
            if k <= i:
                dp[i] = min(dp[i], dp[i - k] + abs(h[i - k]- h[i]))
    print(dp[-1])

if __name__ == "__main__":
    main()
