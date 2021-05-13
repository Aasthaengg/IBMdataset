from scipy.sparse import*
n,_,*L=map(int,open(0).read().split())
s=csgraph.floyd_warshall(csr_matrix((L[2::3],(L[::3],L[1::3])),[n+1]*2),0)
print(sum(s[f,t]<c for f,t,c in zip(*[iter(L)]*3)))