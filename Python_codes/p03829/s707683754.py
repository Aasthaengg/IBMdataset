import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
MOD = 10**9 + 7

x,a,b = map(int,input().split())
li = list(map(int,input().split()))
diff = []
for i in range(len(li)-1):
    c = li[i+1]-li[i]
    diff.append(c)
for i in range(len(diff)):
    diff[i] = min(diff[i]*a,b)
print(sum(diff))