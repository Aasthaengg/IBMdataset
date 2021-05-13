n,m=map(int,input().split())
if abs(n-m)>=2:
    print(0)
    exit()
mod=1000000007
if n==m:
    nf=1
    mf=1
    for i in range(n):
        nf=nf*(n-i)%mod
        mf=mf*(n-i)%mod
    print(int(2*nf*mf%mod))
else:
    if m>n:
        n,m=m,n
    nf=1
    mf=1
    for i in range(n):
        nf=nf*(n-i)%mod
        if i!=n-1:mf=mf*(m-i)%mod
    print(int(nf*mf%mod))
