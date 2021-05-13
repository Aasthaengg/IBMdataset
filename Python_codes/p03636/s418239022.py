# -*- coding: utf-8 -*-
dx = [0, 0, 1, -1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

s = input()
ans = s[0] + str(len(s) - 2) + s[-1]
print(ans)
