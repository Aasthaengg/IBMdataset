import sys
import numpy as np
import itertools
from itertools import product
# from decimal import Decimal
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, m = map(int, readline().split())
k = [list(map(int, readline().split())) for _ in range(m)]
p = list(map(int, readline().split()))

ans = 0
flag = True

for i in product((0, 1), repeat=n):
    #print(i, i[0])

    for j, valK in enumerate(k):
        pp = p[j]
        temp = 0
        for k1, k2 in enumerate(valK):
            if (k1 == 0):
                continue
            else:
                temp += i[k2 - 1]

        if (temp % 2 == pp):
            continue
        else:
            flag = False
            break
    if (flag is False):
        flag = True
        continue
    else:
        ans += 1


print(ans)
