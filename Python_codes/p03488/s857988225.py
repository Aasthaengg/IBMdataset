import numpy as np

s = input()
x_goal, y_goal = map(int, input().split())

directed_x = None
steps = 0
xs = [0]
ys = [0]
for c in (s+'T'):   #sentinel
    if c == 'F':
        steps += 1
    else:
        if directed_x is None:
            x_goal -= steps
            directed_x = True
        elif steps != 0:
            if directed_x:
                xs.append(steps)
            else:
                ys.append(steps)
        steps = 0
        directed_x = not directed_x

dx_2 = sum(xs) - x_goal
if dx_2 % 2 == 1 or dx_2 < 0:
    ans = False
else:
    dx = dx_2 // 2
    possible_x = np.full(dx + 1, False)
    possible_x[0] = True
    for x in xs:
        possible_x[x:] = np.logical_or(possible_x[:len(possible_x)-x], possible_x[x:])
        if possible_x[dx]:
            ans = True
            break
    else:
        ans = False

if ans:
    dy_2 = sum(ys) - y_goal
    if dy_2 % 2 == 1 or dy_2 < 0:
        ans = False
    else:
        dy = dy_2 // 2
        possible_y = np.full(dy + 1, False)
        possible_y[0] = True
        for y in ys:
            possible_y[y:] = np.logical_or(possible_y[:len(possible_y)-y], possible_y[y:])
            if possible_y[dy]:
                ans = True
                break
        else:
            ans = False

if ans:
    print("Yes")
else:
    print("No")