n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

import itertools
pattern = itertools.permutations(xy, n)

import numpy as np

distances = []
for p in pattern:
    distance = 0
    for i, (x, y) in enumerate(p):
        if i == 0:
            base = (x, y)
            continue
    
        b_x, b_y = base
        d2 = (b_x - x) ** 2 + (b_y - y) ** 2
        d = np.sqrt(d2)
        distance += d
    
        base = (x, y)

    distances.append(distance)

print(np.mean(distances))