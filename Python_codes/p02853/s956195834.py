x, y = map(int, input().split())

A, B = [0] * 206, [0] * 206
A[1] = 300000
A[2] = 200000
A[3] = 100000
B[1] = 300000
B[2] = 200000
B[3] = 100000

if x == 1 and y == 1:
    print(A[x] + B[y] + 400000)
else:
    print(A[x] + B[y])