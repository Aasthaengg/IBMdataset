N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

M = sum(A)

for i in range(N):
    K = min(A[i], B[i])
    A[i] -= K
    A[i+1] -= B[i] - K
    A[i+1] = max(0, A[i+1])
    
print(M - sum(A))