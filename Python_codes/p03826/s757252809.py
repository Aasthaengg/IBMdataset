A, B, C, D = map(int, input().split())
x = A * B
y = C * D
if x >= y:
    print(A * B)
else:
    print(C *D)