N = int(input())
B = [int(x) for x in input().split()]
A = [0]*N
A[0]   = B[0]
A[N-1] = B[N-2]
for T in range(0,N-2):
    A[T+1] = min(B[T],B[T+1])
print(sum(A))