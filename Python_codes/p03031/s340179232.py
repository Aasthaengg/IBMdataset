N,M=map(int,input().split())
L=[list(map(int,input().split())) for i in range(M)]
P=list(map(int,input().split()))
c=0
for i in range(2**N):
    A=[0]*N
    for j in range(N):
        if (i>>j&1):
            A[j]=1
    T=True
    for j in range(M):
        s=0
        for k in range(L[j][0]):
            s+=A[L[j][k+1]-1]
        if s%2!=P[j]:
            T=False
    if T:
        c+=1
print(c)