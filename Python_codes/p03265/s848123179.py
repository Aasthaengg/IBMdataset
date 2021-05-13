x1, y1, x2, y2 = map(int, input().split())

a, b = abs(x2 - x1), abs(y1 - y2)

if (x1 <= x2)and(y1 <= y2):
    x3, y3 = x2 - b, y2 + a
    x4, y4 = x3 - a, y3 - b
elif (x1 >= x2)and(y1 <= y2):
    x3, y3 = x2 - b, y2 - a
    x4, y4 = x3 + a, y3 - b
elif (x1 >= x2)and(y1 >= y2):
    x3, y3 = x2 + b, y2 - a
    x4, y4 = x3 + a, y3 + b
elif (x1 <= x2)and(y1 >= y2):
    x3, y3 = x2 + b, y2 + a
    x4, y4 = x3 - a, y3 + b

print(x3, y3, x4, y4)