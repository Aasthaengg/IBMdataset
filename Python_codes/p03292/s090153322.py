a, b, c = list(map(int, input().split()))
s = a, b, c
l = sorted(s)
x, y, z = l
print((z-y)+(y-x))
