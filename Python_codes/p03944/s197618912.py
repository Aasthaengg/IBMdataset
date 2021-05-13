w, h, n = map(int, input().split())
p = [tuple(map(int, input().split())) for _ in range(n)]

x1 = 0
y1 = 0
x2 = w
y2 = h

for x, y, a in p:
    if a == 1:
        if x > x1:
            x1 = x
    elif a == 2:
        if x < x2:
            x2 = x
    elif a == 3:
        if y > y1:
            y1 = y
    elif a == 4:
        if y < y2:
            y2 = y

if x2-x1 > 0 and y2-y1 > 0:
    print((x2-x1)*(y2-y1))
else:
    print(0)
