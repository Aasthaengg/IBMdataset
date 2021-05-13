#!/usr/bin/env python3
h, _, *a = map(int, open(0).read().split())
print("YNeos"[sum(a) < h::2])
