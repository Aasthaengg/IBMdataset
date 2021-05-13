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

mod=10**9+7
n=int(input())
a=lmp()
l=[[0,0] for i in range(60)]
for i in range(n):
    b=format(a[i],"060b")
    for j in range(60):
        if b[j]=="0":
            l[j][0]+=1
        else:
            l[j][1]+=1
ans=0
for i in range(60):
    ans+=(l[i][0]*l[i][1]*(2**(59-i)))%mod
print(ans%mod)