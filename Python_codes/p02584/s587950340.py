#!/usr/bin/env python3

x, k, d = [int(i) for i in input().split(' ')]

moves = abs(x) // d

if moves > k:
    print(abs((abs(x) - k*d )))
else:
    rem = abs(x) % d
    if (k - moves) % 2 == 0:
        print(rem)
    else:
        print(d - rem)
