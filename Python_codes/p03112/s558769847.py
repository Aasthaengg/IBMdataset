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

a,b,q=MI()
lis1=[I() for i in range(a)]
lis2=[I() for i in range(b)]
lis1.append(inf)
lis2.append(inf)
lis1=[-inf]+lis1
lis2=[-inf]+lis2
#print(lis1)
#print(lis2)
for i in range(q):
    u=I()
    x=bisect_left(lis1,u)
    y=bisect_left(lis2,u)
    #print(u,x,y)
    Lll=u-min(lis1[x-1],lis2[y-1])
    Lrr=max(lis1[x],lis2[y])-u
    Llr1=2*(u-lis1[x-1])+(lis2[y]-u)
    Llr2=2*(lis2[y]-u)+u-lis1[x-1]
    Lrl1=2*(u-lis2[y-1])+lis1[x]-u
    Lrl2=2*(lis1[x]-u)+u-lis2[y-1]
    #print(Lll,Lrr,Lrl1,Lrl2,Llr1,Llr2)
    print(min(Lll,Lrr,Lrl1,Lrl2,Llr1,Llr2))
    
    
    
    

