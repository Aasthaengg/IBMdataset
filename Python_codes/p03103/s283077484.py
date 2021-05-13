n,m,*l=map(int,open(0).read().split());c=0
for a,b in sorted(zip(*[iter(l)]*2)):t=min(b,m);c+=a*t;m-=t
print(c)