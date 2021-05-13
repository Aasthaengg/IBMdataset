# -*- coding: utf-8 -*-

x = 0
max_x = 0

N = int(input())
S = list(str(input()))

for i in range(N):
    if S[i] == 'I':
        x += 1
        max_x = max(max_x, x)
    else:   # elseの処理は必ずいれること
        x -= 1
        max_x = max(max_x, x)

print(max_x)