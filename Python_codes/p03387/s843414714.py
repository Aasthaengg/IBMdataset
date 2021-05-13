*A,=sorted(map(int,input().split()))

ans=0
if (A[1]-A[0])%2==0:
    ans=(A[1]-A[0])//2
    ans+=A[2]-A[1]
else:
    ans=(A[1]-A[0])//2+1
    ans+=A[2]+1-A[1]
    
print(ans)