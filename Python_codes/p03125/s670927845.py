#!/usr/bin/env python3
a, b = map(int, open(0).read().split())
if b % a == 0:
    print(a+b)
else:
    print(b-a)
