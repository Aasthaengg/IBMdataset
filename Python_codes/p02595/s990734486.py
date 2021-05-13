n,d,*a=map(int,open(0).read().split())
print(sum((a[i]**2+a[-~i]**2)**0.5<=d for i in range(0,n*2,2)))