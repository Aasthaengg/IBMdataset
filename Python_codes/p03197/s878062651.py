#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
s = sum(i % 2 for i in a)
print("sfeicrosntd"[s > 0::2])
