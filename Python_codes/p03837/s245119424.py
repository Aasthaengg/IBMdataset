from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
n,m,*L=map(int,open(0).read().split())
s=floyd_warshall(csr_matrix((L[2::3],(L[::3],L[1::3])),(n+1,n+1)),0)
ans=0
for f,t,c in zip(*[iter(L)]*3):ans+=s[f,t]<c
print(ans)