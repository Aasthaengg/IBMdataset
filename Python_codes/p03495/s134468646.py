# -*- coding: utf-8 -*-
import collections
N, K=map(int,input().split())
A=list(map(int,input().split()))
C=collections.Counter(A)
KEY=list(C.keys())
count=0
if len(KEY)>K:
    D=len(KEY)-K
    L=C.most_common()[::-1]
    for ii in range(D):
        count+=L[ii][1]

print(count)
    
