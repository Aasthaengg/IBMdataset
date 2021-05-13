n,k,*a=map(int,open(0).read().split());s=t=0;r=range(n)
for i in r:
 for j in r:s+=j>i and a[j]<a[i];t+=a[j]<a[i]
print((s*k+k*~-k//2*t)%(10**9+7))