#!/usr/bin/env python3
x = int(input())
print((x // 11) * 2 + (2 if x % 11 > 6 else 1 if x % 11 != 0 else 0))