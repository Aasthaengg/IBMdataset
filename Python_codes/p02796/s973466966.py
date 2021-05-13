# -*- coding: utf-8 -*-
N = int(input())
items = [list(map(int, input().split())) for i in range(N)]
items = sorted(items, key=lambda x:x[0]+x[1])
res = 0
bf =  -10**9
for x, l in items:
    if bf <= x - l:
        res += 1
        bf = x + l
print(res)
