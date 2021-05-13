N,K=map(int,input().split())
A=list(map(int,input().split()))
for _ in range(K):
  B=[0]*(N+1)
  for i in range(N):
    B[max(0,i-A[i])]+=1
    B[min(N,i+A[i]+1)]-=1
  for i in range(1,N):
    B[i]+=B[i-1]
  if A==B:
    break
  A=B[:]
print(*A[:-1])