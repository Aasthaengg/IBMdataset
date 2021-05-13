r, D, x = map(int, input().split())
A = [r*x-D]
print(A[0])
for i in range(9):
    print(r*A[i]-D)
    A.append(r*A[i]-D)