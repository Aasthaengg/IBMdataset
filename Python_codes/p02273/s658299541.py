from math import sqrt
from collections import deque

sin30 = 1 / 2
cos30 = sqrt(3) / 2
""" Direct length p1-u when p1-p2 is 1 """
p1_to_u = 1 / sqrt(3)


def koch(xy1, xy2):
    global sin30, cos30, p1_to_u
    (x1, y1) = xy1
    (x2, y2) = xy2
    dx, dy = x2 - x1, y2 - y1
    dx3, dy3 = dx / 3, dy / 3
    yield (x1 + dx3, y1 + dy3)
    xu, yu = dx * p1_to_u, dy * p1_to_u
    xu, yu = x1 + cos30 * xu - sin30 * yu, y1 + sin30 * xu + cos30 * yu
    yield (xu, yu)
    yield (x2 - dx3, y2 - dy3)


l = deque(((0.0, 0.0), (100.0, 0.0)))

for _ in range(int(input())):
    new_l = deque()
    prev_xy = l.popleft()
    for xy in l:
        new_l.append(prev_xy)
        new_l.extend(koch(prev_xy, xy))
        prev_xy = xy
    new_l.append(prev_xy)
    l = new_l

for xy in l:
    print(*xy)