x, y, z = map(int,input().split())
a = 0

a = x
x = y
y = a

a = z
z = x
x = a

print(x,y,z)

