#!/usr/bin/env python3
n, *p = map(int, open(0).read().split())
print(sum(p)-max(p)//2)
