#!/usr/bin/env python
import math

n = int(input())
m = math.log10(n)
if int(m) == m:
    print(10)
    exit()

ans = sum(map(int, list(str(n))))
print(ans)
