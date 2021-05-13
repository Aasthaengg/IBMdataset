n,*a=map(int,open(0).read().split())
a.sort()
v=t=0
for i in range(1,n):v+=a[i-1];t=[t,i][2*v<a[i]]
print(n-t)