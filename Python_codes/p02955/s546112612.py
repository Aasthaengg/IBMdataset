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

N,K=map(int,input().split())
A=list(map(int,input().split()))
A.sort(reverse=True)

M=sum(A)
maxi=round(M**.5)+2
lst=[]
i=2

for i in range(1,maxi):
    if M%i==0:
        lst.append(i)
        lst.append(M//i)


lst.sort(reverse=True)
for l in lst:
    B=deque(sorted([i%l for i in A if i%l!=0]))
    _K=K
    #print(B,l)
    while len(B)>=2 and _K:

        n=min(B[0],l-B[-1],_K)
        B[0]-=n
        B[-1]+=n
        _K-=n
        if not B[0]%l:
            B.popleft()
        if not B[-1]%l:
            B.pop()

    if not B:
        print(l)
        exit()
