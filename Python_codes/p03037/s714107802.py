n,m,*a=map(int,open(0).read().split())
b=min(a[1::2])-max(a[::2])+1
print(b if b>0 else 0)