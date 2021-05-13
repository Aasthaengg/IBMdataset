import statistics
n,*a=map(int,open(0).read().split())
b=[q-i for i,q in enumerate(a,1)]
c=statistics.median(b)
ans=sum(map(abs,[p-c for p in b]))
print(int(ans))
