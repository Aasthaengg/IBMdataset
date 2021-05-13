"""from collections import *
from itertools import *
from bisect import *
from heapq import *

import math
from fractions import gcd"""

N,T=map(int,input().split())
A=list(map(int,input().split()))
ruimin=[A[0]]
ruimax=[A[-1]]
for i in range(1,N):
    ruimin.append(min(ruimin[-1],A[i]))
for i in range(0,N-1)[::-1]:
    ruimax.append(max(ruimax[-1],A[i]))
ruimax.reverse()

value=1
lst=[]
for i in range(0,N-1):
    if ruimax[i+1]-A[i]==value:
        lst.append(i)
    elif ruimax[i+1]-A[i]>value:
        value=ruimax[i+1]-ruimin[i]
        lst=[i]

print(len(lst))
