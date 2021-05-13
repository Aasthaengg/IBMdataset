N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

St = sum(A)
for T in range(0,N):
    if A[T]+A[T+1]<= B[T]:
        A[T] = 0
        A[T+1] = 0
    if A[T]<=B[T]<A[T]+A[T+1]:
        A[T+1] = A[T+1]-(B[T]-A[T])
        A[T] = 0
    if B[T]<A[T]:
        A[T] = A[T]-B[T] 
print(St-sum(A))