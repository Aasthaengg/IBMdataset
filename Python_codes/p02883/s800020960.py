import os,io
input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n,k=map(int,input().split())
a=list(map(int,input().split()))
f=list(map(int,input().split()))
a.sort()
a.reverse()
f.sort()
maxproduct=0
for i in range(n):
  maxproduct=max(f[i]*a[i],maxproduct)
l1=0
r1=maxproduct
while True:
  l2=l1
  r2=(l1+r1)//2
  if l2==r2:
    break
  counter=0
  for i in range(n):
    c=r2//f[i]
    while (c+1)*f[i]<=r2:
      c+=1
    counter+=max(0,a[i]-c)
  if counter<=k:
    r1=r2
  else:
    l1=r2
if l1==r1:
  print(r2)
else:
  counter=0
  r2=l1
  for i in range(n):
    c=r2//f[i]
    while (c+1)*f[i]<=r2:
      c+=1
    counter+=max(0,a[i]-c)
  if counter<=k:
    print(l1)
  else:
    print(r1)