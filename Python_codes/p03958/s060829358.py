k,t,*a=map(int,open(0).read().split())
a.sort()
x=a[0]
ans=a[0]
for i in range(1,t):
  if x<a[i]:
    ans=+(a[i]-x)
  else:
    ans=0
  x+=a[i]
print(max(ans-1,0))