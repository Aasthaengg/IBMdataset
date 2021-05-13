n,l=map(int,input().split())
a=list(range(l,n+l))
m=list(map(abs,a))
print(sum(a)-a[m.index(min(m))])