from collections import Counter as C

n = int(input())
blue = C([input() for _ in range(n)])
m = int(input())
red = C([input() for _ in range(m)])

points = dict(blue)
for rk, rv in red.items():
    points[rk] = points.get(rk, 0) - rv
else:
    print(max(0, max(points.values())))