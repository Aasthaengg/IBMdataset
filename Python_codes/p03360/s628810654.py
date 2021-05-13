A=list(map(int,input().split()))
K=int(input())
A.sort(reverse=True)
ans=sum(A)
for i in range(K):
  ans+=A[0]
  A[0]*=2
print(ans)