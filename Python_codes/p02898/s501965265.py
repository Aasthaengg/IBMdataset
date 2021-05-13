n,k,*h=map(int,open(0).read().split())
print(sum([1 if h[i]>=k else 0 for i in range(n)]))