import sys

sys.setrecursionlimit(10 ** 7)
import bisect


# from collections import deque


# map(int, sys.stdin.read().split())


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    dp = [False] * (K + 1)
    dp[0] = False  # 後手の勝ち
    for i in range(K + 1):
        for j in A:
            if j <= i and dp[i-j]==False:
                dp[i] = True
                break
    if dp[K]:
        print("First")
    else:
        print("Second")


if __name__ == "__main__":
    main()
