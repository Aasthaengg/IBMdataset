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
N,M=map(int,input().split())
mod=10**9 + 7
maxi=round(M**.5)+2
fac=[1,1]
for i in range(2,N+100):
    fac.append(fac[i-1]*i%mod)
ifac=[pow(i,mod-2,mod) for i in fac]
sosuu={}
i=2
maxi=round(M**.5)+1
while M>1 and maxi>=i:
    if M%i==0:
        sosuu[i]=0
        while M%i==0:
            M//=i
            sosuu[i]+=1
    i+=1
if M>1:
    sosuu[M]=1
count=1

for s in sosuu:
    a=sosuu[s]
    count=(count*fac[a+N-1]*ifac[N-1]*ifac[a])%mod
print(count)
