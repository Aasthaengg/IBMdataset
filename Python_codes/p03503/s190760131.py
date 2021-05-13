import numpy as np
N=int(input())
#F i,j,k 店i　曜日j 時間帯k
#P 店iと両方回転している時間帯の数がci P：　利益
F=[]
for i in range(N):
    f=list(map(int, input().split()))
    F.append(f)
F=np.array(F)

P=[]
for i in range(N):
    p=list(map(int, input().split()))
    P.append(p)

#N*10
ans=-np.inf
for b in range(1,2**10):
    C=np.zeros(N)
    for i in range(10):
        if b>>i&1==1:
            now=F[:,i]
            C+=now
    subnow=0
    #print(C)
    for j,c in enumerate(C):
        subnow+=P[j][int(c)]
    ans=max(ans, subnow)

print(ans)
