from math import sqrt

n = int(input())
sin60 = sqrt(3) / 2
cos60 = 1 / 2


def koch(x1, y1, x2, y2, depth):
    global sin60, cos60, n
    if depth > n:
        return
    dx, dy = x2 - x1, y2 - y1
    dx3, dy3 = dx / 3, dy / 3
    xs, ys = x1 + dx3, y1 + dy3
    xt, yt = x2 - dx3, y2 - dy3
    xu, yu = xs + cos60 * dx3 - sin60 * dy3, ys + sin60 * dx3 + cos60 * dy3
    depth += 1
    for xy in koch(x1, y1, xs, ys, depth):
        yield xy
    yield (xs, ys)
    for xy in koch(xs, ys, xu, yu, depth):
        yield xy
    yield (xu, yu)
    for xy in koch(xu, yu, xt, yt, depth):
        yield xy
    yield (xt, yt)
    for xy in koch(xt, yt, x2, y2, depth):
        yield xy


print(0.0, 0.0)
for xy in koch(0.0, 0.0, 100.0, 0.0, 1):
    print(*xy)
print(100.0, 0.0)