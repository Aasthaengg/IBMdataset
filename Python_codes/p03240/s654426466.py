from itertools import product
n, *XYH = map(int, open(0).read().split())
for cx, cy in product(range(101), repeat=2):
    B, C = set(), set()
    for x, y, h in zip(XYH[::3], XYH[1::3], XYH[2::3]):
        s = h + abs(x-cx) + abs(y-cy)
        if h:
            C.add(s)
        else:
            B.add(s)
    if len(C) == 1:
        h = C.pop()
        if all(h <= b for b in B):
            print(cx, cy, h)
            exit()