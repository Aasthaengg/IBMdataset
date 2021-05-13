import math

a, b, c = map(int, input().split())

d = c - a
if d <= 0:
    print('No')
else:
    if 4 * a * b < (d - b) ** 2:
        print('Yes')
    else:
        print('No')
