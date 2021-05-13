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
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

A.sort()
B.sort()
C.sort()

lstB=[0 for i in range(N)]
a=0
c=N-1
count=0
#print(A)
#print(B)
#print(C)

for b in range(N)[::-1]:
    while c>=0 and C[c]>B[b]:
        c-=1
    lstB[b]=N-(c+1)
b=N-1
lstA=[0 for i in range(N+1)]
for a in range(N)[::-1]:
    lstA[a]+=lstA[a+1]
    while b>=0 and B[b]>A[a]:
        lstA[a]+=lstB[b]
        b-=1


#print(lstB)
#print(lstA)
print(sum(lstA))
