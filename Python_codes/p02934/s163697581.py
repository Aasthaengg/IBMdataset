#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
m = 1
for i in a:
    m *= i
print(m / sum(m // i for i in a))
