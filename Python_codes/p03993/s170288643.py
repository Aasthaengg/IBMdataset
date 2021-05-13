N,*A=map(int, open(0).read().split())
print(sum(A[A[i-1]-1]==i for i in range(1,N+1))//2)