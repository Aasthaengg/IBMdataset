from math import ceil, floor
k, a, l, r = input(), map(float, raw_input().split()), 2., 2.
for v in a[::-1]:
    l = ceil(l / v) * v
    r = floor(r / v) * v + v - 1
print '%d %d' % (l, r) if l < r else -1
