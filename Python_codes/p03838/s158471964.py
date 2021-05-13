#!/usr/bin/env python3

#import
#import math
#import numpy as np
x, y = map(int, input().split())

ans = abs(abs(x) - abs(y))

if x == 0 or y == 0:
    if x > y:
        ans += 1
elif int(x > 0) ^ int(y > 0):
    ans += 1
else:
    if x > y:
        ans += 2

print(ans)