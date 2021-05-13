n,*l=map(int,open(0).read().split())
c=p=m=0
for i in l:
  c=(c+1)*(i<=p)
  m=max(m,c)
  p=i
print(m)