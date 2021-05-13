import sys
from collections import defaultdict as ddict

N=int(input())
A=map(int,input().split())
Q=int(input())

ct=ddict(int)
tt=0
for x in A:
    ct[x]+=1
    tt+=x

for _ in range(Q):
    q=next(sys.stdin)
    a,b=map(int,q.split())
    ct[b]+=ct[a]
    tt+=ct[a]*b-ct[a]*a
    ct[a]=0
    print(tt)
