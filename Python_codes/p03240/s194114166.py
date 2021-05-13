from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, accumulate, combinations, combinations_with_replacement
from math import sqrt, ceil, floor, factorial
from bisect import bisect_left, bisect_right, insort_left, insort_right
from copy import deepcopy
from operator import itemgetter
from functools import reduce
from fractions import gcd
import sys
def input(): return sys.stdin.readline().rstrip()
def I(): return int(input())
def Is(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def TI(): return tuple(map(int, input().split()))
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def TIR(n): return [TI() for _ in range(n)]
def S(): return input()
def Ss(): return input().split()
def LS(): return list(input())
def SR(n): return [S() for _ in range(n)]
def SsR(n): return [Ss() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
sys.setrecursionlimit(10**6)
MOD = 10**9+7
INF = 10**18
# ----------------------------------------------------------- #

n = I()
XYH = TIR(n)
XYH.sort(key=itemgetter(2), reverse=True)
H = INF
CX = INF
CY = INF
for cx in range(100+1):
    for cy in range(100+1):
        tmp = INF
        for x, y, h in XYH:
            if tmp == INF:
                tmp = h+abs(x-cx)+abs(y-cy)
            elif h != max(tmp - abs(x-cx) - abs(y-cy), 0):
                break
        else:
            H = tmp
            CX = cx
            CY = cy
print("{} {} {}".format(CX, CY, H))
