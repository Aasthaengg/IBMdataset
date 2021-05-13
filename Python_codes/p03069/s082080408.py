from math import ceil,floor,comb,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from queue import Queue,LifoQueue,PriorityQueue
from copy import deepcopy
from time import time
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n = INT()
s = input()
a = [0]*(n+1)
b = [0]*(n+1)
# a[i]: s[:i-1]を白とするための変更個数
# b[i]: s[i:]を黒とするための変更個数

for i in range(1, n+1):
    a[i] = a[i-1] + (1 if s[i-1] == '#' else 0)

for i in range(n-1, -1, -1):
    b[i] = b[i+1] + (0 if s[i] == '#' else 1)

c = [0]*(n+1)
for i in range(n+1):
    c[i] = a[i] + b[i]

print(min(c))