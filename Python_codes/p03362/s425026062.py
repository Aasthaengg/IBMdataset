# -*- coding: utf-8 -*-
N = int(input())

#
lim = 10 ** 5
candidates = [True for _ in range(lim)]
candidates[0], candidates[1] = False, False
for i in range(lim):
    if candidates[i]:
        for j in range(i*2, lim, i):
            candidates[j] = False

#
nums = []
for i in range(lim):
    if candidates[i]:
        if i % 5 == 1:
            nums.append(i)

print(*nums[:N])