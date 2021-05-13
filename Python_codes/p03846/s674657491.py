#!/usr/bin/env python3
from collections import Counter
N = int(input())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7

counters = Counter(A).items()

if N % 2 == 1:
    for k, v in counters:
        if k == 0:
            if v != 1:
                print(0)
                break
        else:
            if k % 2 != 0 or v != 2:
                print(0)
                break
    else:
        ans = pow(2, N // 2, mod)
        print(ans)
else:
    for k, v in counters:
        if k % 2 != 1 or v != 2:
            print(0)
            break
    else:
        ans = pow(2, N // 2, mod)
        print(ans)