n,k,*l=map(int,open(0).read().split())
print([0,sum(sorted(l)[:n-k])][n>k])