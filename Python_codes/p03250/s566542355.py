A, B, C = map(int, input().split())

x = A * 10 + B + C
y = A + 10 * B + C
z = A + B + 10 * C
print(max(x, y, z))