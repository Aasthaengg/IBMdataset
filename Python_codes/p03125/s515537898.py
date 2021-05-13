# -*- coding: utf-8 -*-

# input
A, B = map(int, input().split())

# solve
ans = A + B if B % A == 0 else B - A

# output
print(ans)
