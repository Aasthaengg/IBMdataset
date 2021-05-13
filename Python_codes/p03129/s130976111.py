#!/usr/bin/env python3

n, k = [int(x) for x in input().split()]
print("YES" if n >= k * 2 - 1 else "NO")
