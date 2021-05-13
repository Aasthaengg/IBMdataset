import re
import sys
from collections import *
from functools import lru_cache
from heapq import *
from itertools import *
from statistics import *
from string import (ascii_lowercase as lcletters,
                    ascii_uppercase as ucletters,
                    ascii_letters as letters,
                    digits)

hexdigits='01234567890ABCDEFabcdef'

inf=float('inf')

sys.setrecursionlimit(2**31-1)

rfs=lambda:rl().split()
ri=lambda:int(rl())
ris=lambda:list(map(int,rfs()))
rl=lambda:next(sys.stdin)
rrs=lambda:list(map(str.strip,sys.stdin))
rs=lambda:rl().strip()
rt=lambda:sys.stdin.read()
rg=lambda:list(map(list,rrs()))

def n4(i,j):
    return [
                (i-1,j),
        (i,j+1),        (i,j-1),
                (i+1,j),
    ]

def n8(i,j):
    return [
        (i-1,j-1),(i-1,j),(i-1,j+1),
        (  i,j-1),        (  i,j+1),
        (i+1,j-1),(i+1,j),(i+1,j+1),
    ]

inb=lambda i,j,m,n:0<=i<m and 0<=j<n

###########################################

N=ri()
H=ris()

ok=True
for i in range(N-2,-1,-1):
    x,y=H[i],H[i+1]
    if x-1>y:
        ok=False
        break
    elif x-1==y:
        H[i]-=1

if ok:
    print('Yes')
else:
    print('No')
