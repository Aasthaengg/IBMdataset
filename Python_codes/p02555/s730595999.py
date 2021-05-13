# -*- coding: utf-8 -*-

import numpy as np
S=int(input())

MOD=10**9+7

D=[0]*(S+1)
D[0]=1

L=0
for i in range(3,S+1):
    L+=D[i-3]
    D[i]=L
    D[i]%=MOD

ans=D[S]

print(int(ans))