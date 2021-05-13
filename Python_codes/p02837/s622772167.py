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
a=[]
for i in range(n):
    k=int(input())
    tem=[]
    for j in range(k):
        x,y=mp()
        tem.append([x-1,y])
    a.append(tem)

ans=[0]
for i in range(2**n):
    ch=1
    for k in range(0,n):
        if ((i>>k)&1):
            for q in a[k]:
                if ((i>>q[0])&1)==(q[1]^1):
                    ch=0

    if ch==1:
        ans.append(bin(i).count("1"))
print(max(ans))