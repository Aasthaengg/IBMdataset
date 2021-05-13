import numpy as np


def add(x):
    if x == 1:
        return 300000
    elif x == 2:
        return 200000
    elif x == 3:
        return 100000
    else:
        return 0


n, m = map(int, input().split())

ans = 0
ans += add(n) + add(m)
if n == 1 and m == 1:
    ans += 400000
print(ans)
