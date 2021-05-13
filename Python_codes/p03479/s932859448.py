X, Y = map(int, input().split())
Z = X
c = 0
while Z <= Y:
    c += 1
    Z = 2 * Z
print(c)