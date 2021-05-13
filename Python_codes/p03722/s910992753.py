from bisect import *
from collections import *
from fractions import gcd
from math import factorial
from itertools import *
from heapq import *
import copy
#input()
N,M=map(int,input().split())
ABC=[list(map(int,input().split())) for i in range(M)]

idle_max=10**18+1

dist=[idle_max for i in range(N+1)]
dist[1]=0


for loop in range(N-1):
    for a,b,c in ABC:
        c=-c
        if dist[a] != idle_max:
            dist[b]=min(dist[a] + c,dist[b])

value=dist[N]
for loop in range(N):
    for a,b,c in ABC:
        c=-c
        if dist[a] != idle_max:
            dist[b]=min(dist[a] + c,dist[b])
if value!=dist[N]:
    print("inf")
else:
    print(-value)
