N,K=map(int,input().split())
A=list(map(int,input().split()))
mod=10**9+7

micro=0
for i in range(N):
    for j in range(i):
        if A[i]<A[j]:
            micro+=1
A.sort()
macro=[0]
for i in range(1,N):
    if A[i-1]==A[i]:
        macro.append(macro[-1])
    else:
        macro.append(i)

ans=(micro*K+sum(macro)*K*(K-1)//2)%mod
print(ans)