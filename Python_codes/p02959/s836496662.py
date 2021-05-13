N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
ans=0
for i in range(N):
  ans+=min(A[i]+A[i+1],B[i])
  if A[i]+A[i+1]>=B[i]:
    A[i+1]=min(A[i+1],A[i]+A[i+1]-B[i])
  else:
    A[i+1]=0
print(ans)
