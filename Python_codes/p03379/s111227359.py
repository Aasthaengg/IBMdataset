n,*x=map(int,open(0).read().split())
l,r=sorted(x)[n//2-1:n//2+1]
for i in x: print([l,r][i<r])