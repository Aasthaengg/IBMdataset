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
l=[0]*n
c=0
for i in range(n):
    if s[-1-i]=="W":
        c+=1
    l[-1-i]=c
ans=0
for i in range(n):
    if s[i]=="B":
        ans+=l[i]
print(ans)