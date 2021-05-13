string = input()
x, y = map(int, input().split())

xy = True
x_s = []
y_s = []
cnt = 0
for s in string:
    if s == "F":
        cnt += 1
    else:
        if xy:
            x_s.append(cnt)
            xy = False
        else:
            y_s.append(cnt)
            xy = True
        cnt = 0
if xy:
    x_s.append(cnt)
    xy = False
else:
    y_s.append(cnt)
    xy = True
x_can = [False for _ in range(8001)]
y_can = [False for _ in range(8001)]

x_can[x_s[0]] = True
for xx in x_s[1:]:
    for i in range(8000, xx - 1, -1):
        if x_can[i - xx]:
            x_can[i] = True

y_can[0] = True
for yy in y_s:
    for i in range(8000, yy - 1, -1):
        if y_can[i - yy]:
            y_can[i] = True
            
x_pos = (x + sum(x_s))
y_pos = (y + sum(y_s))
if x_pos % 2 == 1 or y_pos % 2 == 1:
    print("No")
elif x_can[x_pos // 2] and y_can[y_pos // 2]:
    print("Yes")
else:
    print("No")

