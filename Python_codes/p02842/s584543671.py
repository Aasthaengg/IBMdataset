from math import ceil
from math import floor
n = int(input())
x = n / 1.08
if floor(floor(x) * 1.08) == n:
    print(floor(x))
elif floor(ceil(x) * 1.08) == n:
    print(ceil(x))
else:
    print(':(')