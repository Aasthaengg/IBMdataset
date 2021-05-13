n,m=map(int,input().split())
l=[0]*m
for i in range(n):
  a=list(map(int,input().split()))
  for j in range(a[0]):
    l[a[j+1]-1]+=1
z=0
for i in range(m):
  if n==l[i]:
    z+=1
print(z)

