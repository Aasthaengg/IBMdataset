import sys

sys.setrecursionlimit(10000000)
import os
import math
import bisect
import collections
import itertools
import heapq
import re
import queue

# import fractions

ii = lambda: int(sys.stdin.buffer.readline().rstrip())
il = lambda: list(map(int, sys.stdin.buffer.readline().split()))
fl = lambda: list(map(float, sys.stdin.buffer.readline().split()))
iln = lambda n: [int(sys.stdin.buffer.readline().rstrip()) for _ in range(n)]

iss = lambda: sys.stdin.buffer.readline().decode().rstrip()
sl = lambda: list(map(str, sys.stdin.buffer.readline().decode().split()))
isn = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for _ in range(n)]

lcm = lambda x, y: (x * y) // math.gcd(x, y)
# lcm = lambda x, y: (x * y) // fractions.gcd(x, y)

MOD = 10 ** 9 + 7
MAX = float('inf')


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N, M = il()
    A = il()
    matches = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    dict = {i + 1: matches[i] for i in range(9)}
    dp = [-1] * (N + 1)
    dp[0] = 0

    for n in range(N + 1):
        for a in A:
            if n + dict[a] <= N:
                dp[n + dict[a]] = max(dp[n + dict[a]], dp[n] * 10 + a)
    print(dp[N])


if __name__ == '__main__':
    main()
