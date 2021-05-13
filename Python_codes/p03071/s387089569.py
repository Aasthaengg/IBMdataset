a, b = map(int, input().split())

x = a + (a - 1)
y = a + b
z = b + (b - 1)

w = max(x, y, z)

print(w)