
N=int(input())
a=list(map(int,input().split()))

print(2*N-2)
aa=list(map(abs,a))
nmax=aa.index(max(aa))
for i in range(N):
  if i==nmax:
    pass
  else:
    print("{} {}".format(nmax+1,i+1))
if a[nmax]>0:
  for i in range(N-1):
    print("{} {}".format(i+1,i+2))
else:
  for i in range(N-1):
    print("{} {}".format(N-i,N-i-1))
