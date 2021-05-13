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

s = input()

i = 0
j = len(s)-1
ans = 0
while i <= j:
    if s[i] == 'x' and s[j] != 'x':
        while i <= j and s[i] == 'x':
            ans += 1
            i += 1
    elif s[j] == 'x' and s[i] != 'x':
        while i <= j and s[j] == 'x':
            ans += 1
            j -= 1

    if i <= j:
        if s[i] != s[j]:
            print(-1)
            exit()
        i += 1
        j -= 1
    else:
        break

print(ans)