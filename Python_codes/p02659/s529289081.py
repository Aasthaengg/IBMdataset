# Multiplication 3

A, B = input().split()

A = int(A)
b = round(float(B) * 100)

prod100 = A * b

prod = prod100 // 100

print(int(prod))
