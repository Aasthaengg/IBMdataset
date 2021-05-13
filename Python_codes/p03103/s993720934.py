f=lambda:[*map(int,input().split())]
n,m=f()
p=sorted((f()) for _ in range(n))
c=0
for a,b in p:
  if m>b:
    c+=a*b
    m-=b
  else:
    c+=a*m
    break
print(c)