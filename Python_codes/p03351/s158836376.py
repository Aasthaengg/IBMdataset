a, b, c, d = map(int,input().split())

e = a - b
f = b - c
g = c - a

x = abs(e)
y = abs(f)
z = abs(g)

if x <= d and y <= d or z <= d:
    print('Yes')
else:
    print('No')
