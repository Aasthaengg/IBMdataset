N, A, B = map(int, input().split(' '))
H = [int(input()) for _ in range(N)]

import math
def enough(n):
    rest = [h - B * n * 1.0 for h in H]
    m = sum([ math.ceil(r/(A-B)) for r in rest if r > 0])
    return m <= n

l, r = 0, 10**9

while r - l > 1:
    mid = (l + r) // 2
    if enough(mid):
        r = mid

    else:
        l = mid

    # print(l, r, mid)

print(r)
