n,m=map(int,input().split())
lmax,rmin=1,n
for _ in range(m):
    l,r=map(int,input().split())
    lmax=max(lmax,l)
    rmin=min(rmin,r)
print(max(0,rmin-lmax+1))
