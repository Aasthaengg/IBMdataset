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

l=[0]*5
n=int(input())
for i in range(n):
    s=input()
    if s[0]=="M":
        l[0]+=1
    if s[0]=="A":
        l[1]+=1
    if s[0]=="R":
        l[2]+=1
    if s[0]=="C":
        l[3]+=1
    if s[0]=="H":
        l[4]+=1

ans=0
for q in list(itertools.combinations([0,1,2,3,4], 3)):
    c=1
    for i in q:
        c*=l[i]
    ans+=c
print(ans)