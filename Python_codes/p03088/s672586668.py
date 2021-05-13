"""from collections import *
from itertools import *
from bisect import *
from heapq import *

import math
from fractions import gcd"""

N=int(input())
mod=10**9+7
num=pow(4,N,mod)

S={}
for i in range(1,N+1):
    S[i]={}

S[1]={"A":1,"G":1,"C":1,"T":1}
C=["A","G","C","T"]
for i in range(1,N):
    for s in S[i]:
        for c in C:
            st=s+c
            if len(st)>=5:
                st="".join(list(st)[1:])

            if len(st)==3:
                if st in ["AGC","GAC","ACG"]:
                    continue
            elif len(st)==4:
                if "AGC" in st or "GAC" in st or "ACG" in st:
                    continue
                if st[0]+st[1]+st[3]=="AGC":
                    continue
                if st[0]+st[2]+st[3]=="AGC":
                    continue
            if not st in S[i+1]:
                S[i+1][st]=S[i][s]
            else:
                S[i+1][st]+=S[i][s]
                S[i+1][st]%=mod

#print(S)
print(sum([S[N][i] for i in S[N]])%mod)
