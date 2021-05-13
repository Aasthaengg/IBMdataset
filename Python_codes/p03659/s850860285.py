N = int(input())
A = [int(T) for T in input().split()]
L = [0]*(N+1)
R = [sum(A)]*(N+1)
for T in range(0,N):
    L[T+1] = L[T]+A[T]
    R[T+1] = R[T]-A[T]
MIN = 10**10
for T in range(1,N):
    if abs(L[T]-R[T])<MIN:
        MIN = abs(L[T]-R[T])
print(MIN)