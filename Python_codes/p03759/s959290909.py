# -*- coding: utf-8 -*-

# input
a, b, c = map(int, input().split())

# solve
ans = 'YES' if b - a == c - b else 'NO'

# output
print(ans)
