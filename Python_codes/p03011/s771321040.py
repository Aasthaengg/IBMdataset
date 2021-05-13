#!/usr/bin/env python3
(*a, ) = map(int, input().split())
a.sort()
print(sum(a[:2]))
