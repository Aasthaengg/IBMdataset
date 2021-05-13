N,Q=map(int,input().split())
import sys
def input(): return sys.stdin.readline().strip()
STX=[list(map(int,input().split())) for i in range(N)]
D=[int(input()) for i in range(Q)]
X=[]
for s,t,x in STX:
    X.append((s-x,1,x))
    X.append((t-x,-1,x))
X.sort(key=lambda x:x[0])
a=0
k=[]
from heapq import heappop,heappush
kd={}
for x in X:
    while a<Q and D[a]<x[0]:
        if len(k)>0:
            print(k[0])
        else:
            print(-1)
        a+=1
    if x[1]==1:
        heappush(k,x[2])
        if x[2] in kd:
            kd[x[2]]=0
    else:
        kd[x[2]]=1
        while len(k)>0 and k[0] in kd and kd[k[0]]==1:
            heappop(k)
while a<Q:
    print(-1)
    a+=1