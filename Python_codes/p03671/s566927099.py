#!/usr/bin/env python3

a, b, c = map(int, input().split())

ans = min(a+b, min(a+c, b+c))
print(ans)
