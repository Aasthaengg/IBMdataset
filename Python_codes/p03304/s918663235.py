import numpy as np
import collections as col
import math
n, m, d = map(int, input().split())
ans = 0.0

if d == 0:
    ans = (m - 1)/n
else:
    ans = 2.0 * (n - d) * (m - 1) /n/n

# if d == 0:
#     ans = (n - 1)*(m - 1)/n/n
# else:
#     ans = (n - 1)*(m - 1)/n/n/n * 2.0 * (n - d) * (m - 1)

print(ans)
