import decimal
A, B = input().split()
A = decimal.Decimal(A)
B = decimal.Decimal(B)
print(int(A * B))