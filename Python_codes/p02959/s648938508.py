N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

Pre = sum(A)
for T in range(0,N):
    if A[T]<=B[T]:
        A[T+1] = max(A[T+1]-(B[T]-A[T]),0)
        A[T] = 0
    else:
        A[T] -= B[T]
Aft = sum(A)
print(Pre-Aft)