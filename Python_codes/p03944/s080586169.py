#!/usr/bin/env python3
(w, h, n), *q = [[*map(int, i.split())] for i in open(0)]
r = {1: 0, 2: w, 3: 0, 4: h}
for i in q:
    if i[2] == 1:
        r[i[2]] = max(i[0], r[i[2]])
    elif i[2] == 2:
        r[i[2]] = min(i[0], r[i[2]])
    elif i[2] == 3:
        r[i[2]] = max(i[1], r[i[2]])
    elif i[2] == 4:
        r[i[2]] = min(i[1], r[i[2]])
print(
    (r[2] - r[1] if r[2] > r[1] else 0) * (r[4] - r[3] if r[4] > r[3] else 0))
