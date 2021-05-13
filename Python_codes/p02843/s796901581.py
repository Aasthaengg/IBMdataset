#!/usr/bin/env python3
x = int(input())
print("10"[x % 100 > (x // 100) * 5])
