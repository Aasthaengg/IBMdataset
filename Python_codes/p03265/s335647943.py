x1, y1, x2, y2 = map(int, input().split())
muki = x2 - x1
muki2 = y2 - y1
x3, y3, x4, y4 = 0, 0, 0, 0
ax = abs(muki)
ay = abs(muki2)
if muki > 0 and muki2 > 0:
    x3 = x2 - ay
    y3 = y2 + ax
    x4 = x3 - ax
    y4 = y3 - ay
elif muki > 0:
    x3 = x2 + ay
    y3 = y2 + ax
    x4 = x3 - ay
    y4 = y3 + ax
elif muki2 > 0:
    x3 = x2 - ay
    y3 = y2 - ax
    x4 = x3 + ax
    y4 = y3 - ay
else:
    x3 = x2 + ay
    y3 = y2 - ax
    x4 = x3 + ax
    y4 = y3 + ay

print(x3, y3, x4, y4)
