import sys
from collections import deque
from functools import lru_cache
import bisect
import copy
import heapq
import itertools
import math
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]

def main():
    L = input().strip()
    N = len(L)
    dp = [[0] * (N + 1) for _ in range(2)]
    dp[0][0] = 1
    for i, a in enumerate(L):
        if a == "0":
            dp[0][i + 1] = dp[0][i]
            dp[1][i + 1] = (3 * dp[1][i]) % mod
        else:
            dp[0][i + 1] = (2 * dp[0][i]) % mod
            dp[1][i + 1] = (dp[0][i] + 3 * dp[1][i]) % mod

    # print(dp) 
    print((dp[0][N] + dp[1][N]) % mod)


if __name__ == "__main__":
    main()

