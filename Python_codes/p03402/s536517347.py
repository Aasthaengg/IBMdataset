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
import pprint
sys.setrecursionlimit(10 ** 9)


INF = 10 ** 13
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007


a, b = LI()
a -= 1; b -= 1
ans = [['.'] * 100 for _ in range(50)] + [['#'] * 100 for _ in range(50)]


flg = 0
for y in range(99, 50, -2):
    for x in range(0, 100, 2):
        if not a:
            flg = 1
            break
        ans[y][x] = '.'
        a -= 1
    if flg:
        break

flg = 0
for y in range(0, 50, 2):
    for x in range(0, 100, 2):
        if not b:
            flg = 1
            break
        ans[y][x] = '#'
        b -= 1
    if flg:
        break


print(100, 100)
for i in ans:
    print(*i, sep='')
    
