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
from math import floor, ceil,pi,factorial,sin
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

h,w,a,b=MI()
lis=[[0]*w for i in range(h)]
for i in range(b):
    for j in range(w):
        if j<a:
            lis[i][j]=1
        else:
            lis[i][j]=0
#print(lis)
for i in range(h-b):
    for j in range(w):
        if j<a:
            lis[i+b][j]=0
        else:
            lis[i+b][j]=1
#print(lis)
for i in range(h):
    for j in range(w):
        print(lis[i][j],end="")
    print()
            
        



        
    
    


    


    
