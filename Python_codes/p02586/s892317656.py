import sys
import math
import copy
import random
import itertools
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = 10 ** 21
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)

def solve(n=None, s1=None, s2=None):
    r, c, k = getList()
    value = [[0] * (c + 1) for i in range(r)]

    for i in range(k):
        cr, cc, cv = getZList()
        cv += 1
        value[cr][cc + 1] = cv

    dp = [[[0] * (c + 1) for i in range(r)] for j in range(4)]
    # print(value)
    # print("")
    for y in range(r):
        for x in range(1, c+1):
            curv = value[y][x]
            if y > 0:
                dp[0][y][x] = max(
                    dp[0][y-1][x],
                    dp[1][y-1][x],
                    dp[2][y-1][x],
                    dp[3][y-1][x]
                )
                dp[1][y][x] = max(
                    dp[0][y - 1][x] + curv,
                    dp[1][y - 1][x] + curv,
                    dp[2][y - 1][x] + curv,
                    dp[3][y - 1][x] + curv
                )
            if curv == 0:
                for z in range(4):
                    dp[z][y][x] = max(dp[z][y][x], dp[z][y][x-1])

            else:
                dp[0][y][x] = max(dp[0][y][x], dp[0][y][x-1])
                dp[1][y][x] = max(dp[1][y][x], dp[1][y][x-1], dp[0][y][x-1] + curv)
                dp[2][y][x] = max(dp[2][y][x], dp[2][y][x-1], dp[1][y][x - 1] + curv)
                dp[3][y][x] = max(dp[3][y][x], dp[3][y][x-1], dp[2][y][x - 1] + curv)

    # for dd in dp:
    #     print(dd)

    ans = 0
    for z in range(4):
        for y in range(r):
            for x in range(1, c+1):
                ans = max(ans, dp[z][y][x])

    print(ans)

def main():
    n = getN()
    for _ in range(n):
        solve()
    return


if __name__ == "__main__":
    # main()
    solve()

