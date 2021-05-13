N=int(input())
A=[list(map(int,input().split()))for i in range(2)]
ans=0
for i in range(N):
    l=sum(A[0][:i])
    c=A[0][i]+A[1][i]
    r=sum(A[1][i+1:])
    ans=max(ans,l+c+r)
print(ans)