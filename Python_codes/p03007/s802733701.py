n,*a=map(int,open(0).read().split())
a.sort()
u,d=a[-1],a[0]
print(sum(abs(i)for i in a)-2*min(abs(u),abs(d))*(u*d>0))
for i in a[1:-1]:
    if i<0:print(u,i);u-=i
    else:print(d,i);d-=i
print(u,d)