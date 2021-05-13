A = list(map(int, input().split()))
A = sorted(A)
B = str(A[2]) + str(A[1])
print(int(B)+ A[0])