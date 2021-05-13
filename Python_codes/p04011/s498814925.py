A = []
for i in range(4):
    A.append(int(input()))
if A[0] > A[1]:
    print(A[2] * A[1] + A[3] * (A[0]-A[1]))
else:
    print(A[2] * A[0])