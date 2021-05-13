from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce


INF = float('inf')
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007


def main():
    n, k = LI()
    if k > (n - 1) * (n - 2) // 2:
        print(-1)
        return
    else:
        add_v = (n - 1) * (n - 2) // 2 - k
        print(n - 1 + add_v)
        cnt = 0
        for i in range(2, n + 1):
            print(1, i)
        if cnt == add_v:
            return
        for j in range(2, n + 1):
            for l in range(j + 1, n + 1):
                print(j, l)
                cnt += 1
                if cnt >= add_v:
                    return


main()