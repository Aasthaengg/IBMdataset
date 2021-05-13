from math import ceil,floor,comb,factorial,gcd,pow,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heappop,heappush
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

if len(s) < len(t):
    ans = "UNRESTORABLE"
else:
    reg = -1
    for i in range(len(s)-len(t),-1,-1):
        for j in range(len(t)):
            if s[i+j] != '?' and s[i+j] != t[j]:
                break
        else:
            reg = i
            break
    if reg == -1:
        ans = "UNRESTORABLE"
    elif reg == len(s)-len(t):
        s = s[:i]+t
        ans = s.replace('?','a')
    else:
        s = s[:i]+t+s[i+len(t):]
        ans = s.replace('?','a')
print(ans)