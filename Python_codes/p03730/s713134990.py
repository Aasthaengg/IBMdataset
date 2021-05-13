
#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

def int_mtx(N):
    x = []
    for _ in range(N):
        x.append(input())
    return x

def int_map():
    return map(int,input().split())

def int_list():
    return list(map(int,input().split()))

A,B,C = int_map()

l = set()

for i in range(0,B+1):
    l.add((A*i)%B)

if C in l:
    print('YES')
else:
    print('NO')