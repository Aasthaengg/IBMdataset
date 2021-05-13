import fileinput

x1, y1, x2, y2 = map(int, input().split())

xx = x2 - x1
yy = y2 - y1

x3 = x2 - yy
y3 = y2 + xx

x4 = x1 - yy
y4 = y1 + xx

print(x3, y3, x4, y4)