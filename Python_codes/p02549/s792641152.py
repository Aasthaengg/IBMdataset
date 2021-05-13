# coding: utf-8
import sys

# from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
printout = sys.stdout.write
sprint = sys.stdout.flush
# from heapq import heappop, heappush
# from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
# import math
# from itertools import product, accumulate, combinations, product
# import bisect
# import numpy as np
# from copy import deepcopy
#from collections import deque
# from decimal import Decimal
# from numba import jit

INF = 1 << 50
EPS = 1e-8
mod = 998244353


def intread():
    return int(sysread())
def mapline(t=int):
    return map(t, sysread().split())
def mapread(t=int):
    return map(t, read().split())


def run():
    N, K = mapline()
    G = []
    for i in range(K):
        l, r = mapline()
        G.append((l, r))

    dp = [0]* N
    dp[0] = 1
    a = [0] * N
    a[1] = -1
    for k in range(0, N):
        if k >= 1:
            dp[k] = (dp[k-1] + a[k]) % mod
        for l, r in G:
            if k+l <= N-1:
                a[k+l] = (a[k+l] + dp[k]) % mod
            if k+r+1 <= N-1:
                a[k+r+1] = (a[k+r+1] - dp[k]) % mod

    print(dp[N-1])




if __name__ == "__main__":
    run()
