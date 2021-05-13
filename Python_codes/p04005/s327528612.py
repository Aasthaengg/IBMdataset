#!/usr/bin/env python3
(*a, ) = map(int, input().split())
if sum(i % 2 for i in a) > 2:
    print(a[0]*a[1]*a[2]//max(a))
else:
    print(0)
