a, b, c = map(int, input().split())

x = 10 * a + b + c
y = 10 * b + a + c
z = 10 * c + a + b

print(max(x, y, z))