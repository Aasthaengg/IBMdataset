N,*A=map(int,open(0).read().split())
print(sum(i+1==A[A[i]-1]for i in range(N))//2)