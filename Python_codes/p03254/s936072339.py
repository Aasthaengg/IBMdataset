N,X=map(int,input().split())
*A,=map(int,input().split())
A.sort()

ans=0
i=0
while X and i<N-1:
    X-=A[i]
    if X>=0:
        ans+=1
    else:
        break
    i+=1

if i==N-1 and A[i]==X:
    ans+=1

print(ans)