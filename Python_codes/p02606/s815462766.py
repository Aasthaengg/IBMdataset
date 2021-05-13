from math import floor, ceil
l, r, d = map(int, input().split())
print(floor(r/d) - ceil(l/d) +1)