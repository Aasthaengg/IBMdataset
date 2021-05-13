n,k=map(int,input().split())
a=list(map(int,input().split()))
f=list(map(int,input().split()))
a.sort()
f.sort()
f.reverse()

l,r=-1,10**12
while r-l!=1:
  t=(l+r)//2
  c=0
  for i in range(n):
    c+=max(a[i]-t//f[i],0)
  if c<=k:
    r=t
  else:
    l=t
print(r)