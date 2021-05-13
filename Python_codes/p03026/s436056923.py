from scipy.sparse import*
n,*t=map(int,open(0).read().split())
c=sorted(t[-n:])
f=c[:]
for i in csgraph.depth_first_order(csr_matrix((f[1:],(t[:-n:2],t[1:-n:2])),[n+1]*2),1,0,0):n-=1;f[i-1]=c[n]
print(sum(c[:-1]),*f)