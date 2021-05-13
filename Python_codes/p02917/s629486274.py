N=int(input())
B=list(map(int,input().split()))
A=[0]*(N+1)
a=B[-1]
A[N]=a
for i in range(N-2,-1,-1):
  if B[i]<a:
    A[i+1]=B[i]
  A[i]=B[i]
  a=B[i]
print(sum(A))