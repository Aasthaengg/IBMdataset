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

s=input()
n=len(s)
i=0
k=0
l=[[]]
while i<n:
    if s[i]=="A":
        l[k].append(0)
    elif i<n-1:
        if s[i:i+2]=="BC":
            l[k].append(1)
            i+=1
        else:
            l.append([])
            k+=1
    i+=1
ans=0
for lis in l:
    m=len(lis)
    if m>0:
        n1=[0]*m
        c=0
        for i in range(m):
            if lis[-1-i]==1:
                c+=1
            n1[-1-i]=c
        for i in range(m):
            if lis[i]==0:
                ans+=n1[i]
print(ans)