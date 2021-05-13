n,k=map(int,input().split())
c=list(map(int,input().split()))
a=[]
for x in range(n):
  s=c[x]
  t=(s+1)/2
  a.append(t)
  
ans=0
b=[]
b.append(a[0])

for y in range(n-1):
  c=b[y]
  d=b[y]+a[y+1]
  b.append(d)
  
dd=b[k-1]
for z in range(1,n+1-k):
  e=b[z+k-1]-b[z-1]
  
  dd=max(dd,e)

print(dd)