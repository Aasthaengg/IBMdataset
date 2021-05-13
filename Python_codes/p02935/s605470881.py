N,*V=map(int,open(0).read().split())
A=sorted(V)
for n in range(N-1):
    A=sorted([(A[0]+A[1])/2,]+A[2:])
print(A[0])