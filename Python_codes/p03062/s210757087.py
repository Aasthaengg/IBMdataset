import sys
sys.setrecursionlimit(10 ** 9)
# input = sys.stdin.readline    ####
def int1(x): return int(x) - 1
def II(): return int(input())
def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())
def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def MS(): return input().split()
def LS(): return list(input())
def LLS(rows_number): return [LS() for _ in range(rows_number)]
def printlist(lst, k=' '): print(k.join(list(map(str, lst))))
INF = float('inf')
# from math import ceil, floor, log2
# from collections import deque
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
import numpy as np  # cumsum
# from bisect import bisect_left, bisect_right

def solve():
    N = II()
    A = LI()

    dp = np.zeros((N + 1, 2), np.float64)
    dp[0, 1] = -INF  # A[0]より左は存在しないためdp[0, 1]からの派生は存在しない （初期状態でA[0]がフリップされていることはない）
    for i in range(N):
        dp[i + 1, 0] = max(dp[i, 0] + A[i], dp[i, 1] - A[i])
        dp[i + 1, 1] = max(dp[i, 0] - A[i], dp[i, 1] + A[i])
    # print(dp)

    # dp[N, 1]は操作できないため存在しない
    print(int(dp[N, 0]))


if __name__ == '__main__':
    solve()
