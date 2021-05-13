s = int(input())

x1 = 0
y1 = 0
x2 = 10 ** 9
y2 = 1

if s < 10 ** 9:
    y3 = 0
    x3 = s
else:
    mod = s % 10 ** 9
    if mod == 0:
        y3 = s // 10 ** 9
        x3 = 0
    else:
        y3 = s // 10 ** 9 + 1
        x3 = 10 ** 9 - mod

print(x1, y1, x2, y2, x3, y3)
