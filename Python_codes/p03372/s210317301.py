from copy import deepcopy
from itertools import accumulate

n, c = map(int, input().split())
x = []
v = []
# print(n, c)
# c //= 100000000
for _ in range(n):
    _x, _v = map(int, input().split())
    # _x //= 100000000
    # _v //= 100000000
    x.append(_x)
    v.append(_v)
# print(x, v)
v1 = list(accumulate(v)) # CW
v2 = list(accumulate(v[::-1])) # CCW
# print(v1, v2)
f1 = [0] * (n + 1)
f2 = [0] * (n + 1)
for i in range(n):
    f1[i + 1] = v1[i] - x[i]
    f2[i + 1] = v2[i] - (c - x[n - 1 - i])
# print(f1, f2)
g1 = [0] * (n + 1)
g2 = [0] * (n + 1)
for i in range(n):
    g1[i + 1] = max(g1[i], f1[i + 1])
    g2[i + 1] = max(g2[i], f2[i + 1])
# print(g1, g2)
ans = 0
ans = max(ans, g1[n]) # CW only
ans = max(ans, g2[n]) # CCW only
for j in range(n): # CCW then CW
    cal = 0
    cal -= (c - x[n - 1 - j]) * 2
    cal += v2[j]
    cal += g1[n - 1 - j]
    ans = max(ans, cal)
    # print(j, (c - x[n - 1 - j]) * 2, v2[j], g1[n - 1 - j], cal)
for j in range(n): # CW then CCW
    cal = 0
    cal -= (x[j]) * 2
    cal += v1[j]
    cal += g2[n - 1 - j]
    ans = max(ans, cal)
    # print(j, x[j] * 2, v1[j], g2[n - 1 - j], cal)
print(ans)