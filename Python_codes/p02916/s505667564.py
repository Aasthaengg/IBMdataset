N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
ans=0
for x in range(N):
  ans+=B[A[x]-1]
  if x<N-1:
    if A[x]+1==A[x+1]:
      ans+=C[A[x]-1]
print(ans)