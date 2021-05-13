A, B = map(str, input().split())
A = int(A)
B = int(B[0]+B[2]+B[3])
x = A * B
x = x // 100
print(int(x))