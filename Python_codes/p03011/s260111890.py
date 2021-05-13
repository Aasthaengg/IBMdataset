p,q,r=map(int,input().split())
if p>=q and p>=r:
  print(q+r)
elif q>=p and q>=r:
  print(p+r)
else:
  print(p+q)