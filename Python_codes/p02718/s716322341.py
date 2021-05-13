N,M=map(int,input().split())

A=list(map(int,input().split()))
ans=0
A.sort(reverse=True)
S=sum(A)

for i in range(N):
    if A[i]>=S/(4*M):
        ans+=1

if ans>=M:
    print("Yes")
else:
    print("No")
