N,K=map(int,input().split())
A=list(map(int,input().split()))
mod=10**9+7
R=[0]*N
L=[0]*N
for i in range(N):
    r,l=0,0
    a=A[i]
    for j in range(N):
        if i<j:
            if a>A[j]:
                r+=1
        else:
            if a>A[j]:
                l+=1
    R[i]=r
    L[i]=l
ans=0
for i in range(N):
    ans+=K*R[i]+(L[i]+R[i])*(K-1)*K//2%mod
    ans%=mod
print(ans)

