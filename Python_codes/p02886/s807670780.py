#!/usr/bin/env python3
n, *d = map(int, open(0).read().split())
s = sum(d)
print(sum((s - i) * i for i in d)//2)
