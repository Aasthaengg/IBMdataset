import sys
input = sys.stdin.readline

s = input().rstrip()
x, y = [int(x) for x in input().split()]

horizontal = []
vertical = []

switch = 1
distance = 0

for i in range(len(s)):
    if s[i] == "F":
        distance += 1
    elif switch:
        horizontal.append(distance)
        distance = 0
        switch ^= 1
    else:
        vertical.append(distance)
        distance = 0
        switch ^= 1

if switch:
    horizontal.append(distance)
else:
    vertical.append(distance)

dp_x = [[0] * (2 * sum(horizontal) + 1) for _ in range(len(horizontal) + 1)]
dp_y = [[0] * (2 * sum(vertical) + 1) for _ in range(len(vertical) + 1)]

sx = sum(horizontal)
sy = sum(vertical)

if not (-sx <= x <= sx and -sy <= y <= sy):
    print("No")
    exit()

dp_x[0][0 + sx] = 1
dp_y[0][0 + sy] = 1
dp_x[1][horizontal[0] + sx] = 1

for i in range(2, len(horizontal) + 1):
    x_ = horizontal[i - 1]
    for j in range(-sx, sx + 1):
        if -sx <= j - x_ <= sx: 
            dp_x[i][j + sx] = max(dp_x[i][j + sx], dp_x[i - 1][j - x_ + sx])
        if -sx <= j + x_ <= sx:
            dp_x[i][j + sx] = max(dp_x[i][j + sx], dp_x[i - 1][j + x_ + sx])


for i in range(1, len(vertical) + 1):
    y_ = vertical[i - 1]
    for j in range(-sy, sy + 1):
        if -sy <= j - y_ <= sy: 
            dp_y[i][j + sy] = max(dp_y[i][j + sy], dp_y[i - 1][j - y_ + sy])
        if -sy <= j + y_ <= sy:
            dp_y[i][j + sy] = max(dp_y[i][j + sy], dp_y[i - 1][j + y_ + sy])

if dp_x[-1][x + sx] and dp_y[-1][y + sy]:
    print("Yes")
else:
    print("No")