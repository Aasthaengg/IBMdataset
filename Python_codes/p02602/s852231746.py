n,k,*a=map(int,open(0).read().split())
for i in range(n-k):
  if a[i]<a[i+k]:
    print("Yes")
  else:
    print("No")
