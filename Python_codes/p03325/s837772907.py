#!/usr/bin/env python3
print(sum(bin(i)[::-1].find("1") for i in [*map(int, open(0).read().split())][1:]))
