# -*- coding: utf-8 -*-
import sys
from collections import defaultdict

N,P=map(int, sys.stdin.readline().split())
S=sys.stdin.readline().strip()
S=S[::-1]

ans=0
if P in (2,5):
    len_S=len(S)
    for i,x in enumerate(S):
        x=int(x)
        if x%P==0:
            ans+=(len_S-i)
    print ans
else:
    L=[0] 
    val=0
    for i,x in enumerate(S):
        x=int(x)
        val+=pow(10,i,P)*x
        L.append(val%P)

    C=defaultdict(lambda: 0)
    for x in L:
        ans+=C[x]
        C[x]+=1
    print ans
