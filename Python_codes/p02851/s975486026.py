n,k,*a=map(int,open(0).read().split())
a=[0]+a
for i in range(n):a[i+1]=(a[i+1]-1+a[i])%k
d={}
c=0
for i,b in enumerate(a):
  v=d.get(b,0)
  c+=v
  d[b]=v+1
  j=i-k+1
  if j>=0:d[a[j]]=d.get(a[j],0)-1
print(c)