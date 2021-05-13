from collections import *
from heapq import *
from itertools import *
from fractions import gcd
import sys
from decimal import *
import copy
input=lambda :sys.stdin.readline().rstrip()


H,W,K=map(int,input().split())
S=[input() for i in range(H)]

value=H+W-1
if H==1:
    count=0
    countL=0
    w=0
    while w<W:
        if S[0][w]=="1":
            count+=1
        if count>K:
            countL+=1
            count=0
        else:
            w+=1
    print(countL)
else:
    for i in range(2**(H-1)):
        lst=[i>>m&1 for m in range(H-1)]#0なら線がある
        count=[0 for i in range(lst.count(0)+1)]
        count_zero=copy.copy(count)
        idx={}
        c=0
        for h in range(H-1):
            idx[h]=c
            if lst[h]==0:
                c+=1
        idx[H-1]=c
        flag=0
        w=0
        pre_w=0
        countL=lst.count(0)
        while w<W:
            for h in range(H):

                if S[h][w]=="1":
                    count[idx[h]]+=1
            if max(count)>K:
                if pre_w==w:
                    flag=1
                    break

                pre_w=w
                countL+=1
                count=copy.copy(count_zero)
            else:
                w+=1

        if not flag:
            value=min(value,countL)
    print(value)
