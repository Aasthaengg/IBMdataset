x,y,z,w = map(int, input().split())

p = z + y - w
q = w + z - x
r = x + y - w
s = y + z - x
print(p,q,r,s)