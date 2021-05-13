N=int(input())
A,B=[0]*N,[0]*N
for i in range(N):
  A[i],B[i]=map(int,input().split())
ans=A[0]+B[0]
for i in range(N):
  ans=min(ans,A[i]+B[i])
print(ans)