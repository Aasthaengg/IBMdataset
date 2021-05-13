import sys
def input():
    return sys.stdin.readline()[:-1]
from itertools import permutations
N,M,R=map(int,input().split())
r=list(map(lambda x: int(x)-1,input().split()))
l=tuple(permutations(range(R)))
C=[[10**8]*N for i in range(N)]
for i in range(M):
    a,b,c=map(int,input().split())
    C[a-1][b-1]=c
    C[b-1][a-1]=c
for i in range(N):
    C[i][i]=0
for i in range(N):
    for j in range(N):
        for k in range(N):
            C[j][k] = min(C[j][k],C[j][i] + C[i][k])
a=10**8
for i in l:
    t=0
    for j in range(R-1):
        t+=C[r[i[j]]][r[i[j+1]]]
    if a>t:
        a=t
print(a)