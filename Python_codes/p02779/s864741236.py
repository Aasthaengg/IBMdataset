#!/usr/bin/env python3
_, *a = open(0).read().split()
print("YNEOS"[len(a) != len({*a})::2])
