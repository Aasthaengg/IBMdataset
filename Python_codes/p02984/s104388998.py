N=int(input())
A=list(map(int,input().split()))
S=sum(A)
X=S
for i in range(1,N-1,2):
    X-=2*A[i]
ans=[X]

for j in range(N-1):
    ans.append(2*A[j]-ans[j])
print(*ans)