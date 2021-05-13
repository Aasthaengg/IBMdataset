# -*- coding: utf-8 -*-

import sys
import os
import math


N = int(input())


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

cnt = 0
for i in range(N):
    v = int(input())
    if is_prime(v):
        cnt += 1

print(cnt)