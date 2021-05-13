n,k,*a=map(int,open(0).read().split())
mod=10**9+7
x=0
y=0
for i in range(n-1):
  for j in range(i+1,n):
    if a[i]>a[j]:
      x+=1
for i in range(n):
  for j in range(n):
    if a[i]<a[j]:
      y+=1
print((x*k+y*k*(k-1)//2)%mod)