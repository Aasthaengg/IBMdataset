n, a, b = map(int, input().split())
h = [int(input()) for _ in range(n)]

import math

def C(d):
    sum = 0
    for i in range(n):
        sum += math.ceil(max(h[i] - b * d, 0) / (a - b))
    return sum <= d

lb = -1
ub = 10 ** 9 + 1
while (ub - lb) > 1:
    mid = (lb + ub) // 2
    if C(mid):
        ub = mid
    else:
        lb = mid
print(ub)
