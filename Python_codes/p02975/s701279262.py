n,*a=map(int,open(0).read().split())
ans=a[0]
for i in range(1,n):
  ans^=a[i]
print('Yes' if ans==0 else 'No')