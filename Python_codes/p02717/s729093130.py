x, y, z = map(int, input().split())
x ^= y
y ^= x
x ^= y
x ^= z
z ^= x
x ^= z
print(x, y, z)
