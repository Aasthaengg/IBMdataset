#!/usr/bin/env python3

n = [int(x) for x in input().split()]
print("YES" if sorted(n) == [1, 4, 7, 9] else "NO")
