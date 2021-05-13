import math

xyz = input().split()
x = int(xyz[0])
y = int(xyz[1])
z = int(xyz[2])

num = math.ceil(x/y)

print(z*num)
