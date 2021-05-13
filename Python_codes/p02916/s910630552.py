N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]
Total = sum(B)
for T in range(0,N-1):
    if A[T+1]-A[T]==1:
        Total += C[A[T]-1]
print(Total)