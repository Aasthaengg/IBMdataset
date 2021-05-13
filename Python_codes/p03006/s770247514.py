from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,groupby,permutations,combinations,product,combinations_with_replacement
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
x = [LIST() for i in range(n)]
 
a = []
for i in range(n):
    for j in range(n):
        if i != j:
            a.append((x[j][0]-x[i][0], x[j][1]-x[i][1]))
 
a.sort()
count = 1
reg = 1

for i in range(1, len(a)):
    if a[i][:] == a[i-1][:]:
        count += 1
        reg = max(reg, count)
    else:
        count = 1

if n == 1:
    ans = n
else:
    ans = n - reg

print(ans)