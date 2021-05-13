#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N, K = map(int, input().strip().split())
s = input()
res = ''
for i in range(N):
    if i == K - 1:
        res += s[i].lower()
    else:
        res += s[i]
print(res)
