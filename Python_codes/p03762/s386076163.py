I=lambda:[int(i)for i in input().split()]
n,m=I()
N=I()
M=I()
F=lambda x,y:sum(j*(y-1-2*i)for i,j in enumerate(x))
print(F(N,n)*F(M,m)%(10**9+7))