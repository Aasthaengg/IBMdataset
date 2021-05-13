#!/usr/bin/env python3

a = [int(x) for x in input().split()]
print("Yes" if len(set(a)) == 1 else "No")
