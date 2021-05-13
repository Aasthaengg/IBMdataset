from itertools import product
n, *XYH = map(int, open(0).read().split())
X, Y, H = XYH[::3], XYH[1::3], XYH[2::3]
A = []
for cx, cy in product(range(101), repeat=2):
    B = set()
    C = set()
    for x, y, h in zip(X, Y, H):
        s = h + abs(x-cx) + abs(y-cy)
        if h == 0:
            B.add(s)
        else:
            C.add(s)
    if len(C) == 1:
        h = C.pop()
        if all(h <= b for b in B):
            A.append((cx, cy, h))
print(*A.pop())