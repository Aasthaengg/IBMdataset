N,*A=map(int,open(0).read().split())
A=len(set(A))
print((A-1,A)[A&1])