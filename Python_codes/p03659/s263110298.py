n=int(input())
A=[int(i) for i in input().split()]

x=sum(A)
y=0
ans=10**16

for i in range(n-1):
    x-=A[i]
    y+=A[i]
    ans=min(ans,abs(x-y))

print(ans)