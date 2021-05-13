import sys
import math

n, h = map(int, input().split())
a = 0
b = []

for i in range(n):
    x, y = map(int, input().split())
    a = max(a, x)
    b.append(y)

b.sort(reverse=True)

b = [x for x in b if x > a]

for i, x in enumerate(b):
    h -= x
    if h <= 0:
        print(i + 1)
        sys.exit()

if len(b) == 0:
    i = -1

ans = i + 1 + math.ceil(h / a)

print(ans)