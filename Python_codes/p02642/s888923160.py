n=int(input())
A=list(map(int,input().split()))

m=max(A)

X=[0]*(m+1)

A.sort()

for i in range(n):
    for j in range(A[i],m+1,A[i]):
        X[j]+=1

ans=0

for i in range(n):
    if X[A[i]]==1:
        ans+=1
print(ans)