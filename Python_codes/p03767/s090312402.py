#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
a.sort()
print(sum(a[i] for i in range(n, 3 * n, 2)))
