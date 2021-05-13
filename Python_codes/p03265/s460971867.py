x1, y1, x2, y2 = map(int, input().split())
l = x2-x1
h = y2-y1

x3 = x2-h
y3 = y2+l
x4 = x1-h
y4 = y1+l

print(x3, y3, x4, y4)