from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf,comb
from itertools import accumulate,groupby,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from queue import Queue,LifoQueue,PriorityQueue
from copy import deepcopy
from time import time
from functools import reduce
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

s = input()
a = [0]*26

if len(s) != 26:
    for x in s:
        a[ord(x)-ord('a')] += 1
    for i in range(26):
        if a[i] == 0:
            tmp = i
            break
    ans = s + chr(ord('a')+tmp)
else:
    if s == "zyxwvutsrqponmlkjihgfedcba":
        ans = -1
    else:
        for i in range(len(s)-1, -1, -1):
            k = ord(s[i])-ord('a')
            j = 1
            while k + j < 26:
                if a[k+j] == 0:
                    j += 1
                else:
                    tmp = k + j
                    break
            else:
                a[k] += 1
                continue
            tmp2 = i
            break
        ans = s[:tmp2] + chr(tmp+ord('a'))
print(ans)