N,M=map(int, input().split())
A,C=[],[]
for i in range(N):
  a,b=map(int, input().split())
  A.append((a,b))
for i in range(M):
  a,b=map(int, input().split())
  C.append((a,b,i+1))

for i in range(N):
  long=10**9
  ans=-1
  for j in range(M):
    d=abs(A[i][0]-C[j][0])+abs(A[i][1]-C[j][1])
    if long>d:
      ans=C[j][2]
      long=d
  print(ans)