#!/usr/bin/env python3
sx, sy, tx, ty = map(int, input().split())
x = tx - sx
y = ty - sy
h = abs(sx - tx)
v = abs(sy - ty)
ans = [[1, 0]] * h + [[0, 1]] * v + [[-1, 0]] * h + [[0, -1]] * v
ans += [[0, -1]] + [[1, 0]] * -~h + [[0, 1]] * -~v + [[-1, 0]]
ans += [[0, 1]] + [[-1, 0]] * -~h + [[0, -1]] * -~v + [[1, 0]]
if x < 0 and y < 0:
    ans = [*map(lambda x: [-x[0], -x[1]], ans)]
elif x < 0:
    ans = [*map(lambda x: [-x[1], x[0]], ans)]
elif y < 0:
    ans = [*map(lambda x: [x[1], -x[0]], ans)]

for i in ans:
    if i == [1, 0]:
        print("R", end="")
    elif i == [-1, 0]:
        print("L", end="")
    elif i == [0, 1]:
        print("U", end="")
    else:
        print("D", end="")
print("")
