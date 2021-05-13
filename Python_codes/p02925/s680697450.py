"""from collections import *
from itertools import *
from bisect import *
from heapq import *

import math
from fractions import gcd"""
import copy
N=int(input())
A=[list(reversed(list(map(int,input().split())))) for i in range(N)]
for i in range(N):
    for m in range(N-1):
        A[i][m]-=1

playerlst=set([i for i in range(N)])

count=0
nlst=copy.copy(playerlst)
while playerlst:
    flag=0
    lst=set()
    playedlst=set()
    while nlst:
        p=nlst.pop()
        if not p in lst and p in playerlst:
            p2=A[p][-1]
            if not p2 in lst and p2 in playerlst:
                if A[p2][-1]==p:
                    flag=1
                    A[p].pop()
                    A[p2].pop()
                    lst.add(p)
                    lst.add(p2)
                    if p2 in nlst:
                        nlst.remove(p2)
                    playedlst.add(p)
                    playedlst.add(p2)
                    if not A[p]:
                        playerlst.remove(p)
                    if not A[p2]:
                        playerlst.remove(p2)
    if not flag:
        print(-1)
        exit()
    count+=1
    nlst=copy.copy(playedlst)
print(count)
