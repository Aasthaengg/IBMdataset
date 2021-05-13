x, y, z = map(int, input().split())
tmp = 0

tmp = x
x = y
y = tmp
tmp = x
x = z
z = tmp

print(x, y, z, sep=' ')