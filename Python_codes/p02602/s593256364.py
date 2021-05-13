_,k,*a=map(int,open(0).read().split())
for a,b in zip(a,a[k:]):print('YNeos'[a>=b::2])