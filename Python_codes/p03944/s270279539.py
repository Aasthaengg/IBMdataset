w, h, n = map(int, input().split())
x_reg = 0
y_reg = 0

for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1 and x_reg < x:
        x_reg = x
    if a == 2 and w > x:
        w = x
    if a == 3 and y_reg < y:
        y_reg = y
    if a == 4 and h > y:
        h = y

x_edge = max(0, w-x_reg)
y_edge = max(0, h-y_reg)

print(x_edge*y_edge)