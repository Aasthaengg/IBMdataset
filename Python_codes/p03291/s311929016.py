from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial


INF = float('inf')
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LIM(): return list(map(lambda x:int(x) - 1, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def LIRM(n): return [LIM() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
mod = 1000000007


s = S()
n = 1
a = ab = abc = 0
for i in s:
    if i == 'A':
        a = (a + n) % mod
    elif i == 'B':
        ab = (ab + a) % mod
    elif i == 'C':
        abc = (abc + ab) % mod
    else:
        abc = (abc * 3 + ab) % mod
        ab = (ab * 3 + a) % mod
        a = (a * 3 + n) % mod
        n = n * 3 % mod





print(abc)