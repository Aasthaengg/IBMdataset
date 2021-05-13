n,*l=map(int,open(0).read().split())
n//=2
l.sort()
print(l[n]-l[~n])