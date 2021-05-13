#!/usr/bin/env python3
n, *p = map(int, open(0).read().split())
print(sum(sorted(p[i - 1:i + 2])[1] == p[i] for i in range(1, n - 1)))
