A = [int(i) for i in input().split()]
A = sorted(A)
print(abs(A[1] - A[0]) + abs(A[2] - A[1]))