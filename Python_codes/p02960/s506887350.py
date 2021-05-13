import sys
import math
import bisect
import heapq
from collections import Counter


def input():
    return sys.stdin.readline().rstrip()


def main():
    mod = 10 ** 9 + 7
    S = list(input())
    l = len(S)
    dp = [[0] * 13 for _ in range(l + 1)]

    dp[0][0] = 1
    for j in range(1, l + 1):
        jp = j - 1
        if S[jp] == "?":
            for k in range(13):
                kk = k * 10
                for q in range(10):
                    new_k = (kk + q) % 13
                    dp[j][new_k] += dp[jp][k]
            for k in range(13):
                dp[j][k] %= mod
        else:
            n = int(S[jp])
            for k in range(13):
                new_k = (k * 10 + n) % 13
                dp[j][new_k] += dp[jp][k]
                dp[j][new_k] %= mod
    print(dp[l][5])


if __name__ == "__main__":
    main()
