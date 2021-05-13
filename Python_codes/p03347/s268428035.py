from collections import *
from heapq import *
from itertools import *
from fractions import gcd
import sys
from decimal import *
import copy
from bisect import *
input=lambda :sys.stdin.readline().rstrip()
N=int(input())
A=[int(input()) for i in range(N)]
if A[0]>0:
    print(-1)
    exit()
for i in range(N-1):
    if A[i]+1<A[i+1]:
        print(-1)
        exit()



count=A[-1]
for i in range(1,N)[::-1]:

    if A[i-1]==A[i]-1:
        pass
    else:
        count+=A[i-1]
print(count)
