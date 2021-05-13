#!/usr/bin/env python3
c = eval(input().replace(" ", "+"))
print(c // 2 * (c % 2 < 1) or "IMPOSSIBLE")
