from bisect import*
b=bisect_left
n,q,*t=map(int,open(0).read().split())
p=t[-q:]
*a,=o=[-1]*q
for x,t,s in sorted(zip(*[iter(t[~q::-1])]*3)):
 l,r=b(p,s-x),b(p,t-x)
 while l<r:
  if~o[l]:l=o[l]
  else:a[l],o[l]=x,r;l+=1
print(*a)