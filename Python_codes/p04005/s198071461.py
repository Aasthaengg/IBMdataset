a, b, c = map(int, input().split())

x = b * c if a % 2 == 1 else 0
y = a * c if b % 2 == 1 else 0
z = a * b if c % 2 == 1 else 0
print(min(x, y, z))
