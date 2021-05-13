n,*a = map(int,open(0).read().split())
a = sorted([a[i] -i for i in range(n)])
print(sum([abs(i - a[n//2]) for i in a]))