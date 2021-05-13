import copy

n,x=map(int,input().split())

a=[int(x) for x in input().split()]
aa=copy.deepcopy(a)

ans=0
for i in range(n):
  if x<a[i]:
    a[i]=x

for i in range(n-1):
  if x<a[i]+a[i+1]:
    a[i+1]=x-a[i]

ans=sum(aa[i]-a[i] for i in range(n))
print(ans)