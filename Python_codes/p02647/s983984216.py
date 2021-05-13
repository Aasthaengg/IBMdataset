import math
N,K=map(int,input().split())
A=[0]*N
A=list(map(int,input().split()))

da=[0 for i in range(N)]
for k in range(K):
    B=[0 for i in range(N)]
    for i in range(N):
        l=max(0,i-A[i])
        r=min(N-1,i+A[i])
        B[l]=B[l]+1
        if(r+1<N):
            B[r+1]=B[r+1]-1
    for i in range(1,N):
        B[i]=min(N,B[i]+B[i-1])
    if(A==B):
        break
    A=B
b=[str(i) for i in B]
b=" ".join(b)
print(b)
