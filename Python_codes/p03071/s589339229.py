A = sorted(list(map(int, input().split())), reverse=True)
print(A[0]*2 if A[0] == A[1] else A[0]+(A[0]-1))