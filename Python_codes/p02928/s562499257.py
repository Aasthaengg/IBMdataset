N,K=map(int,input().split())
A=list(map(int,input().split()))

mod=10**9+7

B=[]
for i in range(N):
    l=0
    r=0
    for j in range(i):
        if A[i]>A[j]:
            l+=1

    for k in range(i,N):
        if A[i]>A[k]:
            r+=1
    B.append([l,r])

ans=0
for i in range(N):
    ans+=B[i][0]*(K-1)*K//2+B[i][1]*K*(K+1)//2
ans%=mod

print(ans)