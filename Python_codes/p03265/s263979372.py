x1, y1, x2, y2 = map(int, input().split())

a, b = x2 - x1, y2 - y1
x3, y3 = x2 - b, y2 + a
x4, y4 = x1 - b, y1 + a

print(x3, y3, x4, y4)