N,*A=map(int,open(0).read().split());M=max(A);m=min(A);s=range(1,N+1);p=print;p(2*N-1);v,d=-m<M and(M,1)or(m,-1);r=s[::d]
for i in s:p(A.index(v)+1,i)
for z in zip(r,r[1:]):p(*z)