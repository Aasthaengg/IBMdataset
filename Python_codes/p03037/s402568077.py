n,m=map(int, input().split())
lmax=0
rmin=1000000
for i in range(m):
  l,r=map(int, input().split())
  lmax=max(l, lmax)
  rmin=min(r, rmin)

if rmin-lmax>=0:
  print(rmin-lmax+1)
else:
  print(0)