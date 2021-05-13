import math
def li():
    return list(map(int, input().split()))
def mi():
    return map(int, input().split())
def ii():
    return int(input())

x1, y1, x2, y2 = mi()

l = 0
# x = Cの場合
if (x2 - x1) == 0:
    l = abs(y2 - y1)
    if y2 > y1:
        x3 = x1 - l
    else:
        x3 = x1 + l
    y3 = y2
    x4 = x3
    y4 = y1
# y = Cの場合
elif (y2 - y1) == 0:
    l = abs(x2 - x1)
    x3 = x2
    if x2 > x1:
        y3 = y2 + l
    else:
        y3 = y2 - l
    x4 = x1
    y4 = y3
# y = ax + bの場合
else:
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x1 - (y2 - y1)
    y4 = y1 + (x2 - x1)

print(x3, y3, x4, y4)