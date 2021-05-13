# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 09:11:30 2020

@author: NEC-PCuser
"""

n, m = map(int, input().split())
cnt = [[] for _ in range(n + 1)]
for i in range(m):
    p, y = map(int, input().split())
    cnt[p].append([y, i])
buf = [-1] * m
for i in range(len(cnt)):
    if not cnt[i]:
        continue
    cnt[i].sort()
    for j in range(len(cnt[i])):
        buf[cnt[i][j][1]] = '{:06d}{:06d}'.format(i, j + 1)
print('\n'.join(buf))