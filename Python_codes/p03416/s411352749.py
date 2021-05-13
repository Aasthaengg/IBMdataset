# -*- coding: utf-8 -*-

A, B = map(int, input().split())

ans = 0
tmp_left = ''
tmp_right = ''

for x in range(A, B + 1):
    tmp_left = str(x)[0] + str(x)[1]
    tmp_right = str(x)[-1] + str(x)[-2]
    if tmp_left == tmp_right:
        ans += 1

print(ans)