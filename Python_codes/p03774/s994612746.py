n,m=map(int,input().split())
A=[]
C=[]
for i in range(n):
  a,b=map(int,input().split())
  A.append([a,b])
for j in range(m):
  c,d=map(int,input().split())
  C.append([c,d])
for i in range(n):
  dis=10**9
  ans=0
  for j in range(m):
    if abs(A[i][0]-C[j][0])+abs(A[i][1]-C[j][1])<dis:
      dis=abs(A[i][0]-C[j][0])+abs(A[i][1]-C[j][1])
      ans=j+1
  print(ans)