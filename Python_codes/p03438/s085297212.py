n,*a=map(int,open(0).read().split())
print("Yes" if sum((j-i)//2*2 if j-i>0 else 2*(j-i)for i,j in zip(a[:n],a[n:]))>=0 else "No")