n,a,b,*l=map(int,open(0).read().split())
t,p=0,l[0]
for i in l:
  t+=min(a*(i-p),b)
  p=i
print(t)