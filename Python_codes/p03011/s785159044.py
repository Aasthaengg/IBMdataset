p,q,r=map(int,input().split())
if p>=q and p>r:
    print(q+r)
if q>=r and q>p:
    print(p+r)
if r>=p and r>q:
    print(q+p)
if r==p and p==q:
    print(q+p)