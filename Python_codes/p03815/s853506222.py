import math
x = int(input())
it = math.ceil(x / 11)
if (it * 5 + it * 6) - x >= 5:
    print(it * 2 - 1)
else:
    print(it * 2)
