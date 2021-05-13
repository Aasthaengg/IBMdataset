N=int(input())
*A,=map(int,input().split())
A.sort()
ans=1
S=0
i=0
while i+1<N:
    S+=A[i]
    if 2*S>=A[i+1]:
        ans+=1
    else:
        ans=1
    i+=1
print(ans)