from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, accumulate, combinations, combinations_with_replacement, groupby
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
INF = float('inf')
# ----------------------------------------------------------- #

n, k = Is()
s = S()
A = []  # group count of 1, 0 (1, 0, 1, 0, ... , 1)
if s[0] == "0":
    A.append(0)
for key, value in groupby(s):
    A.append(len(list(value)))
if s[-1] == "0":
    A.append(0)
# print(A)
ans = 0
w = 2*k+1
tmp = sum(A[:w])
ans = max(ans, tmp)
for i in range(w+1, len(A)+1, 2):
    tmp -= A[i-1-w] + A[i-w]
    tmp += A[i-1] + A[i]
    ans = max(ans, tmp)

print(ans)
