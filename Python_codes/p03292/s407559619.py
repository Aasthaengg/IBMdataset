A = map(int, input().split())
A = list(sorted(A))
print(abs(A[0]-A[1])+abs(A[1]-A[2]))