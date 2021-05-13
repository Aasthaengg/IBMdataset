n,*b=map(int,open(0).read().split())
print(b[0]+sum(min(b[i],b[i+1]) for i in range(n-2))+b[-1])