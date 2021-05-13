import re
import sys
from collections import *
from functools import lru_cache
from heapq import *
from itertools import *
from statistics import *
from string import (
    ascii_letters as letters,
    ascii_lowercase as lcletters,
    ascii_uppercase as ucletters,
    digits
)

xdigits='01234567890ABCDEFabcdef'
inf=float('inf')
bigi=2**31-1

cache=lru_cache(None)

sys.setrecursionlimit(bigi)

rfs=lambda:rl().split()
ri=lambda:int(rl())
ris=lambda:list(map(int,rfs()))
rl=lambda:next(sys.stdin)
rrs=lambda:list(map(str.strip,sys.stdin))
rs=lambda:rl().strip()
rt=lambda:sys.stdin.read()
rg=lambda:list(map(list,rrs()))
rig=lambda:[[*map(int,x.split())] for x in rls()]

def nbs4(i,j):
    return [
                (i-1,j),
        (i,j-1),        (i,j+1),
                (i+1,j),
    ]

def nbs8(i,j):
    return [
        (i-1,j-1),(i-1,j),(i-1,j+1),
        (  i,j-1),        (  i,j+1),
        (i+1,j-1),(i+1,j),(i+1,j+1),
    ]

inb=lambda i,j,m,n:0<=i<m and 0<=j<n

###########################################

N,Q=ris()
S=rs()
a=[0]*(N+1)
for i in range(1,N):
    if S[i-1]=='A' and S[i]=='C':
        a[i+1]+=1
    a[i+1]+=a[i]
for _ in range(Q):
    l,r=ris()
    print(a[r]-a[l])
