#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import division, print_function, absolute_import, unicode_literals

import sys

N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))

h = [None] * N

if T[-1] != A[0]:
    print(0)
    sys.exit()

odd = False
h[0] = T[0]
for i, (a, b) in enumerate(zip(T[1:], T[:-1]), 1):
    if a != b:
        h[i] = a
    if a < b:
        odd = True
        break

if odd is True:
    print(0)
    sys.exit()

if h[-1] is None:
    h[-1] = A[-1]
elif h[-1] != A[-1]:
    print(0)
    sys.exit()

for i, (a, b) in enumerate(zip(A[::-1][1:], A[::-1][:-1]), 1):
    if a != b:
        if h[N-i-1] is None:
            h[N-i-1] = a
        elif h[N-i-1] != a:
            odd = True
            break
    if a < b:
        odd = True
        break

if odd is True:
    print(0)
    sys.exit()

i = 1
a, b = 0, 0
cnt = 0
ans = 1
flag = False
while i < N-1:
    if h[i] is None:
        flag = True
        a = h[i-1]
        cnt = 0
        while h[i] is None:
            i += 1
            cnt += 1
        b = h[i]
        # print(a, b, cnt)
        ans = (ans * (min(a, b) ** cnt)) % (10 ** 9 + 7)
        # print(ans)
    else:
        i += 1

# check
# print(h)
odd = False
for i in range(N):
    if h[i] != None:
        cm = h[i]
    if T[i] < cm:
        # print(i, cm, T[i])
        odd = True
        break
cm = None
for i in range(N):
    if h[N-i-1] != None:
        cm = h[N-i-1]
    if A[N-i-1] < cm:
        # print('hoge')
        # print(N-i-1, cm, A[N-i-1])
        odd = True
        break
if odd is True:
    print(0)
    sys.exit()

print(ans)
