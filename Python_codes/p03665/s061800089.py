n,p=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n):a[i]%=2
o=a.count(1)
z=n-o
if o==0:
  if p==0:print(2**z)
  else:print(0)
else:
  print(2**(n-1))