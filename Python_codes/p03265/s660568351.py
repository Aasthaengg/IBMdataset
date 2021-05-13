x1, y1, x2, y2 = map(int, input().split())

xl = x2-x1
yl = y2-y1

x3 = x2 - yl
y3 = y2 + xl
x4 = x1 - yl
y4 = y1 + xl

print(x3, y3, x4, y4)