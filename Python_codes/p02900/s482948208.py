from math import ceil,floor,comb,factorial,gcd,pow,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from copy import deepcopy
from time import time
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

a, b = MAP()
n = gcd(a, b)
s = sorted(divisor(n))
t = [1]*len(s)

ans = 0
for i in range(1, len(s)-1):
    if t[i] == 0:
        continue
    else:
        for j in range(i+1, len(s)):
            if t[j] == 0:
                continue
            else:
                if s[j] % s[i] == 0:
                    t[j] = 0
print(sum(t))