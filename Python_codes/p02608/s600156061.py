# coding: utf-8
import math
import itertools

n = int(input())

ans = [0] * n

for x, y, z in itertools.product(range(1, int(math.sqrt(n))), range(1, int(math.sqrt(n))), range(1, int(math.sqrt(n)))):
    idx = x**2 + y**2 + z**2 + x*y + y*z + z*x
    if idx <= n:
        ans[idx-1] += 1

print(*ans, sep="\n")