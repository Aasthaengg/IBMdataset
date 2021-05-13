N,K=map(int,input().split())
A=list(map(int,input().split()))
B=[0]*(N+1)
C=0
for i in range(K):
  for j in range(N+1):
    B[j]=0
  for j in range(N):
    B[max(0,j-A[j])]+=1
    B[min(N,j+A[j]+1)]-=1
  C=0
  for j in range(N):
    C+=B[j]
    A[j]=C
  if set(A)==set([N]):
    break
print(*A)