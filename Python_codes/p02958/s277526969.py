#!/usr/bin/env python3
n, *p = map(int, open(0).read().split())
print("YNEOS"[sum(p[i] != i+1 for i in range(n)) not in (0, 2)::2])
