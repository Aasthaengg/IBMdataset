#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,k = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
r=0
for i in range(0,k):
  r=r+p[i]
print(r)
