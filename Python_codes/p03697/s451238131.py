# -*- coding: utf-8 -*-

# input
A, B = map(int, input().split())

# solve
ans = (A + B) if (A + B) < 10 else "error"

# output
print(ans)
