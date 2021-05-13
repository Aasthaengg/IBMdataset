X, Y = map(int, input().split())
Z = X
C = 0
while Z <= Y:
    Z *= 2
    C += 1
print(C)