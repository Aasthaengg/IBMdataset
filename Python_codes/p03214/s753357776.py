N=int(input())
*A,=map(int,input().split())

S=sum(A)
i=0
while i<N:
    A[i]*=N
    i+=1

now=float('inf')
i=0
while i<N:
    if abs(S-A[i])<now:
        now=abs(S-A[i])
        ans=i
    i+=1

print(ans)