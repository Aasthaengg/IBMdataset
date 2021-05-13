n,*a=map(int,open(0).read().split())
s=len(set(a))
print(s if (n-s)%2==0 else s-1)