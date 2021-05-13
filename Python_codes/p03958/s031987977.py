#!/usr/bin/env python3
k, t, *a = map(int, open(0).read().split())
print(max(max(a)*2 - 1 - k, 0))
