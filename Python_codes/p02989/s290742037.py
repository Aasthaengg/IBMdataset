n,*d=map(int,open(0).read().split())
l,r=sorted(d)[n//2-1:n//2+1]
print(r-l)