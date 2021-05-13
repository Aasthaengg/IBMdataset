#import decimal
#decimal.getcontext().prec==500 Floatの桁数を500まで増やす
#Decimal(c).sqrt() それで平方根を求める
#Decimal(1) / Decimal(7) 1/7
from collections import *
from itertools import *
from bisect import *
from heapq import *
import copy
import math
from fractions import gcd
import sys
#input = sys.stdin.readline


#N=int(input())
N,M,P=map(int,input().split())
ABC=[list(map(int,input().split())) for i in range(M)]
for i in range(M):
    ABC[i][2]=-1*(ABC[i][2]-P)
data=[[] for i in range(N+1)]
for a,b,c in ABC:
    data[b].append(a)

idle_max=10**9




visited=set()
stack=[N]
while stack:
    a=stack.pop()
    for p in data[a]:
        if not p in visited:
            visited.add(p)
            stack.append(p)




data=[idle_max for i in range(N+1)]
data[1]=0
for i in range(N-1):
    for a,b,c in ABC:
        if data[a] != idle_max:
            data[b]=min(data[b],data[a]+c)
predata=copy.copy(data)
value=data[N]
for i in range(N):
    for a,b,c in ABC:
        if data[a] != idle_max:
            data[b]=min(data[b],data[a]+c)

for i in visited:
    if predata[i]>data[i]:
        break
else:
    print(max(-value,0))
    exit()
print(-1)
