n,*a=map(int,open(0).read().split())
a.sort()
v=t=0
for i in range(1,n):
 v+=a[i-1]
 if 2*v<a[i]:t=i
print(n-t)