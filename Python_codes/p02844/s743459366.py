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
s=input()
l=[0]*1000
for _ in range(n):
    i=s[_]
    for j in range(1000):
        k=str(j).zfill(3)
        if k[0]==i and l[j]==2:
            l[j]=3
        if k[1]==i and l[j]==1:
            l[j]=2
        if k[2]==i and l[j]==0:
            l[j]=1
ans=0
for i in l:
    if i==3:
        ans+=1
print(ans)