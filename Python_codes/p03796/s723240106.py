p = 10**9+7
N = int(input())
A = [1 for _ in range(N+1)]
for i in range(2,N+1):
    A[i] = (A[i-1]*i)%p
print(A[N])