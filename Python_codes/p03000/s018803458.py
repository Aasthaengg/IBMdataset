# -*- coding: utf-8 -*-

n, x = map(int, input().split())
ll = list(map(int, input().split()))

d = 0
ans = 1

for l in ll:
    d += l

    if d > x:
        break


    ans += 1

print(ans)
