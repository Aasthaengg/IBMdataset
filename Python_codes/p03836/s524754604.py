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

x1,y1,x2,y2=MI()
dx=x2-x1
dy=y2-y1
for i in range(dx):
    print("R",end="")
for i in range(dy):
    print("U",end="")
for i in range(dx):
    print("L",end="")
for i in range(dy):
    print("D",end="")
print("L",end="")
for i in range(dy+1):
    print("U",end="")
for i in range(dx+1):
    print("R",end="")
print("D",end="")
print("R",end="")
for i in range(dy+1):
    print("D",end="")
for i in range(dx+1):
    print("L",end="")
print("U")

            

    
    
        
