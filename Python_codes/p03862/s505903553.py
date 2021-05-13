N,X=map(int,input().split())
A=list(map(int,input().split()))

A_sum=sum(A)
A[0]=min(X,A[0])

for i in range(N-1):
    if A[i]+A[i+1]>X:
        A[i+1]=X-A[i]
print(A_sum-sum(A))