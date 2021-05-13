n,*l=map(int,open(0).read().split())
l.sort()
v=sum(l[:2])
for i in range(2,n): v=v/2+l[i]
print(v/2)