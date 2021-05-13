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

hexdigits='01234567890ABCDEFabcdef'
inf=float('inf')

sys.setrecursionlimit(2**31-1)

rfs=lambda:rl().split()
ri=lambda:int(rl())
ris=lambda:list(map(int,rfs()))
rls=lambda:list(sys.stdin)
rl=lambda:next(sys.stdin)
rrs=lambda:list(map(str.strip,rls()))
rs=lambda:rl().strip()
rt=lambda:sys.stdin.read()
rg=lambda:list(map(list,rrs()))
rig=lambda:[[*map(int,x.split())] for x in rls()]

def n4(i,j):
    return [
                (i-1,j),
        (i,j-1),        (i,j+1),
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

N,Q=ris()

adj=defaultdict(list)
for _ in range(N-1):
    a,b=ris()
    adj[a].append(b)
    adj[b].append(a)

ct=[0]*N
for _ in range(Q):
    p,x=ris()
    ct[p-1]+=x
    
def dfs(u,p):
    if p!=-1:
        ct[u-1]+=ct[p-1]
    for v in adj[u]:
        if v!=p:
            dfs(v,u)

dfs(1,-1)

print(*ct)
