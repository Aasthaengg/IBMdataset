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

n=input()
l=[0]*len(n)
l[0]=int(n[0])
for i in range(1,len(n)):
    l[i]=l[i-1]+int(n[i])
ans=l[-1]
for i in range(len(n)):
    ans=max(ans,l[i]-1+9*(len(n)-1-i))
print(ans)