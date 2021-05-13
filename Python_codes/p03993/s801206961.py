n,*a=map(int,open(0).read().split())
a=[0]+a
ans=0
for i in range(1,n+1):
  if i==a[a[i]]:
    ans+=1
print(ans//2)