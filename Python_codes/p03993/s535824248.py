N=int(input())
*A,=map(int,input().split())
i=0
ans=0
while i<N:
    if i+1==A[A[i]-1]:
        ans+=1
    i+=1
print(ans//2)