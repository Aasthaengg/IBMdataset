#float型を許すな
#numpyはpythonで
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7

n,m=MI()
lis=[LI() for i in range(n)]
lis.sort(key=lambda x:x[0])
#print(lis)
j=0
ans=0
i=0
while j<n and i<m:
    #print(i,j,ans)
    if lis[j][1]>0:
        lis[j][1]-=1
        ans+=lis[j][0]
        i+=1
    else:
        j+=1
print(ans)