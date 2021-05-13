N,K=map(int,input().split())
A=list(map(int,input().split()))*2

mod=10**9+7

inside=0
for i in range(N-1):
    for j in range(i+1,N):
        if A[i]>A[j]:
            inside+=1

outside=0
for i in range(N):
    for j in range(N,2*N):
        if A[i]>A[j]:
            outside+=1
    
#print(inside,outside)
print((inside*K+outside*(K-1)*K//2)%mod)