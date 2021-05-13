k,*a = map(int,open(0).read().split())
a = a[::-1]
nmax = 2
nmin = 2
for i in range(k):
  if nmax//a[i]-(nmin-1)//a[i]<=0:
    print(-1)
    exit()
  nmin = ((nmin-1)//a[i]+1)*a[i]
  nmax = (nmax//a[i])*a[i]+a[i]-1
print(nmin,nmax)