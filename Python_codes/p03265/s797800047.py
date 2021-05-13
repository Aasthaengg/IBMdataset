x,y,z,w = map(int, input().split())
u = (x-z,y-w)
v = (w-y, x-z)
x1, y1 = z - v[0] ,w - v[1]
z1,w1 = x1 + u[0], y1 + u[1]
print(x1, y1, z1, w1)