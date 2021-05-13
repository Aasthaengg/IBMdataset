a, b, c, d = map(int, input().split())

import itertools

max_xy = max(a * c, b * c, a * d, b * d)

print(max_xy)