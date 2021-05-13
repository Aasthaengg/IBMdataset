n,k,*l=map(int,open(0).read().split())
l.sort()
print(min(l[k+i-1]-l[i] for i in range(n-k+1)))