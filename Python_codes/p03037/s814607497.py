N,M=map(int,input().split())
lmax,rmin=1,N
for i in range(M):
  l,r=map(int,input().split())
  if l > lmax:lmax=l
  if r < rmin:rmin=r
print(max(rmin-lmax+1,0))