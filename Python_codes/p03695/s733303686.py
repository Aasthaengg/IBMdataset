n,*a=map(int,open(0).read().split())
l=[i//400 for i in a if i<3200]
c=len(set(l))
print(max(1,c),c+n-len(l))