n,m=map(int,input().split())
A=[0]*n
for i in range(m):
  a,b=map(int,input().split())
  A[a-1]+=1
  A[b-1]+=1
f=0
for i in range(n):
  if A[i]%2==1:
    f=1
if f==0:
  print("YES")
else:
  print("NO")