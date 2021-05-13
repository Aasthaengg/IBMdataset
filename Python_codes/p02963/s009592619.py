S = int(input())
lim = 10 ** 9

import math
y3 = math.ceil(S / lim)
x3 = lim * y3 - S

# print(lim * y3 - 1 * x3)

ans = list(map(str, [0, 0, lim, 1, x3, y3]))
print(' '.join(ans))

