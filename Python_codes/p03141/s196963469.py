import sys
import heapq
import math
import fractions
import bisect
import itertools
from collections import Counter
from collections import deque
from operator import itemgetter
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

n=int(input())
a=[0]*n
b=[0]*n
l=[0]*n
for i in range(n):
    x,y=mp()
    a[i]=x
    b[i]=y
    l[i]=[x,y,x+y]
l=sorted(l,key=lambda X: X[2],reverse=True)
ans=0
for i in range(n):
    if i%2==0:
        ans+=l[i][0]
    else:
        ans-=l[i][1]
print(ans)