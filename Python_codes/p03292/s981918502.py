A = list(map(int, input().split()))

A = sorted(A)
print(A[1]-A[0] + A[2]-A[1])
