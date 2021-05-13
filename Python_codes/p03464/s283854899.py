#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

"""
AGC020 B
"""

k = int(input())
alist = list(map(int, input().split()))
alist.reverse()

pmax = 2
pmin = 2

for a in alist:
    ma = a*(pmax//a)
    q, r = divmod(pmin, a)
    if r == 0:
        mi = a*q
    else:
        mi = a*q+a
    if ma < mi:
        print(-1)
        exit()
    pmax = ma+a-1
    pmin = mi

print(pmin, pmax)

