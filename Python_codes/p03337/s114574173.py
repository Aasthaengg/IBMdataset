A, B = map(int, input().split())

x = A + B
y = A - B
z = A * B

s = sorted([x, y, z])
print(s[-1])