import re
import sys
from collections import *
from functools import lru_cache
from heapq import *
from itertools import *

INF=float('inf')

sys.setrecursionlimit(2**31-1)

rfs=lambda:rl().split()
ri=lambda:int(rl())
ris=lambda:list(map(int,rfs()))
rl=lambda:next(sys.stdin)
rls=lambda:list(map(str.strip,sys.stdin))
rs=lambda:rl().strip()
rt=lambda:sys.stdin.read()
rg=lambda:list(list(ln) for ln in rls())

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

H,W=ris()
s=rg()

nbl=sum(row.count('#') for row in s)
s[0][0]='#'
que=deque([(0,0,1)])
ok=False
while que:
    i,j,k=que.popleft()
    if i+1==H and j+1==W:
        ok=True
        break
    for ni,nj in n4(i,j):
        if inb(ni,nj,H,W) and s[ni][nj]!='#':
            s[ni][nj]='#'
            que.append((ni,nj,k+1))

if ok:
    print(H*W-nbl-k)
else:
    print(-1)
