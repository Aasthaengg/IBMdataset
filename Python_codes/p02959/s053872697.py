
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

ans=0

for i in reversed(range(1,N+1)):
    if A[i]<B[i-1]:
        ans+=A[i]
        B[i-1]=B[i-1]-A[i]
        A[i]=0
    else:
        ans+=B[i-1]
        A[i]=A[i]-B[i-1]
        B[i-1]=0

    if A[i-1]<B[i-1]:
        ans+=A[i-1]
        B[i-1]=B[i-1]-A[i-1]
        A[i-1]=0
    else:
        ans+=B[i-1]
        A[i-1]=A[i-1]-B[i-1]
        B[i-1]=0
    
print(ans)