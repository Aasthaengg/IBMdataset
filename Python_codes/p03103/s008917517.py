f=lambda:map(int,input().split())
n,m=f()
l=sorted(list(f()) for _ in range(n))
c=0
for a,b in l:
  if b>m: c+=a*m; break
  c+=a*b; m-=b
print(c)