#!/usr/bin/env python3
(*a, ) = map(int, input().split())
a.sort()
b = a[-1] - a[-2]
c = a[1] - a[0]
print(b + -(-c // 2) + c % 2)
