# -*- coding: utf-8 -*-

N,A,B = map(int, input().split())

dist = B - A
if dist % 2 == 0:
    ans = "Alice"
else:
    ans = "Borys"

print(ans)