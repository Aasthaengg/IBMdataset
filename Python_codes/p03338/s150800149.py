# -*- coding: utf-8 -*-

N = int(input())
S = list(str(input()))
ans = 0

for i in range(1, N):
    x = set(S[0:i])
    y = set(S[i:])
    intrsect_x_y = x & y
    ans = max(ans, len(intrsect_x_y))

print(ans)