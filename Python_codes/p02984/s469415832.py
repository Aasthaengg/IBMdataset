N=int(input())
A=list(map(int,input().split()))
s=sum(A)

ans=[]
ans.append(s-2*sum(A[1::2]))
for i in range(1,N):
  ans.append(2*A[i-1]-ans[-1])
print(*ans)
