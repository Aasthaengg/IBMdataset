N=int(input())
*A,=map(int,input().split())
now=A[0]
i=1
ans=0
while i<N:
    if A[i]==now:
        ans+=1
        A[i]+=100
    now=A[i]
    i+=1
print(ans)