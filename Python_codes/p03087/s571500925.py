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

n,q=mp()
s=input()
ans=[0]*(n+1)
c=0
for i in range(1,n):
    if s[i-1]=="A" and s[i]=="C":
        c+=1
    ans[i+1]=c
for i in range(q):
    r,l=mp()
    print(ans[l]-ans[r])