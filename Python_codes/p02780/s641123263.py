# Template 1.0
import sys, re
from collections import deque, defaultdict, Counter, OrderedDict
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from heapq import heappush, heappop, heapify, nlargest, nsmallest
def STR(): return list(input())
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def list2d(a, b, c): return [[c] * b for i in range(a)]
def sortListWithIndex(listOfTuples, idx):   return (sorted(listOfTuples, key=lambda x: x[idx]))
def sortDictWithVal(passedDic):
    temp = sorted(passedDic.items(), key=lambda kv: (kv[1], kv[0]))
    toret = {}
    for tup in temp:
        toret[tup[0]] = tup[1]
    return toret
def sortDictWithKey(passedDic):
    return dict(OrderedDict(sorted(passedDic.items())))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

n,k = MAP()

p = LIST()
#
# i=0
# j = k-1

mx = 0

for i in range(k):
    mx+=(p[i]+1)/2
    # print(mx)
gndMax = mx
i = 1
j=k
# print(mx)
while(j<n):
    mx = mx + (p[j] + 1) / 2 - (p[i - 1] + 1) / 2
    gndMax=max(gndMax, mx)
    i+=1
    j+=1
    # print(mx, gndMax)
print(gndMax)
