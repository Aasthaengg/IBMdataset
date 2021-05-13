N = int(input())
A = list(map(int,input().split()))

S = sum(A)
x1 = S - 2*sum(A[1::2])
 
X = [x1] * (N)
for i in range(1,N):
    X[i] = 2*A[i-1] - X[i-1]
 
print(' '.join([str(xi) for xi in X]))