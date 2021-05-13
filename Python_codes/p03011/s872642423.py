p, q, r = map(int,input().split())
x = p+q
y = q+r
z = r+p
print(min(x, y, z))