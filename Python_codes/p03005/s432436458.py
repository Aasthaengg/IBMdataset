#!/usr/bin/env python3

n, k = [int(x) for x in input().split()]
print(n - k if k != 1 else 0)
