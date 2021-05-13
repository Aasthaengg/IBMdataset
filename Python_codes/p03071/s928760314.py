# -*- coding: utf-8 -*-

cnt = 0
l = sorted(list(map(int, input().split())), reverse=True)

cnt = cnt + l[0]

l[0] = l[0] - 1

l = sorted(l, reverse=True)

cnt = cnt + l[0]

print(cnt)