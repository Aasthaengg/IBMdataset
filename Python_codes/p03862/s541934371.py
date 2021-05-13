N,X=map(int,input().split())
*A,=map(int,input().split())

ans=0
if A[0]>X:
    ans+=A[0]-X
    A[0]=X

i=1
while i<N:
    if A[i]+A[i-1]>X:
        ans+=A[i]+A[i-1]-X
        A[i]=X-A[i-1]
    i+=1
        
print(ans)