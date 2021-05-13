k,n=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
b=0
for i in range(n-1):
  d=a[i+1]-a[i]
  b=max(b,d)
d=a[0]-(a[n-1]-k)
b=max(d,b)
print(k-b)