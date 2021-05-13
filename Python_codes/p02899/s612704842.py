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
a=lmp()
l=[]
for i in range(n):
    l.append([a[i],1+i])
l=sorted(l,key=lambda x:x[0])
ans=[]
for i in range(n):
    ans.append(l[i][1])
print(*ans)