import fractions
N=int(input())
T,A=map(int,input().split())
for i in range(1,N):
    nT,nA=map(int,input().split())
    if(nT>=T and nA>=A):
        T,A=nT,nA
        continue
    pT,pA=T//nT,A//nA
    if(T%nT!=0):
        pT+=1
    if(A%nA!=0):
        pA+=1
    T,A=nT*max(pT,pA),nA*max(pT,pA)
print(T+A)