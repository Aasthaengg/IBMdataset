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
t = input()
a = [0]*26
b = [0]*26

for i in range(len(s)):
    x = ord(s[i])-ord('a')
    y = ord(t[i])-ord('a')
    a[x] += 1
    b[y] += 1

if sorted(a) == sorted(b):
    print("Yes")
else:
    print("No")