import numpy as np
N=int(input())

F=[]
for i in range(N):
    f=list(map(int, input().split()))
    F.append(f)

P=[]
for i in range(N):
    p=list(map(int, input().split()))
    P.append(p)

F=np.array(F)
P=np.array(P)

ans=-np.inf

for b in range(1,2**10):
    now=0
    L=np.zeros(N)
    for i in range(10):
        if b>>i&1==1:
            L+=F[:,i]
    for i in range(N):
        now+=P[i,int(L[i])]
    ans=max(ans, now)

print(ans)