A = list(map(int, input().split()))
print('A' if abs(A[0]-A[1]) <= abs(A[0]-A[2]) else 'B')