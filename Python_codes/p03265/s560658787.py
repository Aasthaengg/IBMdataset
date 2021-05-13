x1, y1, x2, y2 = [int(w) for w in input().split()]
b = x2 - x1
a = y2 - y1

x3 = x2-a
y3 = y2+b

x4 = x3-b
y4 = y3 - a

print(x3, y3, x4, y4)

