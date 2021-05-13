from scipy.sparse import*
n,*t=map(int,open(0).read().split())
c=sorted(t[-n:])[::-1]
f=find(c)[0]
f[csgraph.depth_first_order(csr_matrix((f[1:],(t[:-n:2],t[1:-n:2])),[n+1]*2),1,0,0)-1]=c
print(sum(c[1:]),*f)