n = int(input())
x0 = 0
y0 = 0
x1 = 1
y1 = 10 ** 9
x2 = (n - 1) // y1 + 1
y2 = (y1 - n) % y1
print(x0, y0, x1, y1, x2, y2)