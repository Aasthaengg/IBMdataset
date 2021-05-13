# E - Bomber

from collections import Counter

h, w, m = map(int, input().split())
hw = [tuple(map(int, input().split())) for i in range(m)]

ys, xs = zip(*hw)
ymax, = Counter(ys).most_common(1)
xmax, = Counter(xs).most_common(1)

bombed = max(ymax[1], xmax[1])

if bombed < m:
    if ymax[1] > xmax[1]:
        hw2 = [(a, b) for a, b in hw if a != ymax[0]]
        _, xs = zip(*hw2)
        xmax, = Counter(xs).most_common(1)
        bombed += xmax[1]
    else:
        hw2 = [(a, b) for a, b in hw if b != xmax[0]]
        ys, _ = zip(*hw2)
        ymax, = Counter(ys).most_common(1)
        bombed += ymax[1]

print(bombed)
