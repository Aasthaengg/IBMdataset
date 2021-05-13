N=int(input())
*A,=map(int,input().split())

ans=0
i=0
j=1
while i<N:
    if A[i]==j:
        j+=1
    else:
        ans+=1
    i+=1

print([-1,ans][1 in A])