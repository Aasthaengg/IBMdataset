"""from collections import *
from itertools import *
from bisect import *
from heapq import *

import math
from fractions import gcd"""
S=input()
x,y=map(int,input().split())

Xlst=[]
Ylst=[]
count=0
flag=0
for s in S:
    if s=="F":
        count+=1
    else:
        if flag:
            if count:
                Ylst.append(count)
            flag=0
        else:
            if count:
                Xlst.append(count)
            flag=1
        count=0
if flag:
    if count:
        Ylst.append(count)
else:
    if count:
        Xlst.append(count)

if S[0]=="T":
    numx=set([0])
else:
    numx=set([Xlst[0]])
nlst=set()
c=0
for i in range(0 if 0 in numx else 1,len(Xlst)):
    X=Xlst[i]
    if c%2==0:
        while numx:
            a=numx.pop()
            nlst.add(a+X)
            nlst.add(a-X)
    else:
        while nlst:
            a=nlst.pop()
            numx.add(a+X)
            numx.add(a-X)
    c+=1
if x in numx|nlst:
    numx=set([0])
    nlst=set()
    c=0
    for X in Ylst:
        if c%2==0:
            while numx:
                a=numx.pop()
                nlst.add(a+X)
                nlst.add(a-X)
        else:
            while nlst:
                a=nlst.pop()
                numx.add(a+X)
                numx.add(a-X)
        c+=1
    if y in numx|nlst:
        print("Yes")
    else:
        print("No")
else:
    print("No")
