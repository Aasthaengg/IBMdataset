# author:  Taichicchi
# created: 17.09.2020 23:35:32

import sys

a, b, c = map(int, input().split())


s = (c - a - b) ** 2 - 4 * a * b


if (s > 0) & (c - a - b > 0):
    print("Yes")
else:
    print("No")
