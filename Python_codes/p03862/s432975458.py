N,x=map(int, input().split())
A=list(map(int, input().split()))
ans=0
ans+=max(0,A[0]-x)
A[0]=min(A[0],x)
if A[0]+A[1]>x:
    ans+=A[1]-(x-A[0])
    A[1]=x-A[0]
ans+=max(0,A[-1]-x)
A[-1]=min(A[-1],x)
if A[-2]+A[-1]>x:
    ans+=A[-2]-(x-A[-1])
    A[-2]=x-A[-1]
for i in range(1,N-1):
    if A[i-1]+A[i]>x:
        ans+=A[i]-(x-A[i-1])
        A[i]=x-A[i-1]
print(ans)