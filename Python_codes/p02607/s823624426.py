N = int(input())
A = [int(X) for X in input().split()]
print(sum(True for T in range(1,N+1,2) if A[T-1]%2==1))