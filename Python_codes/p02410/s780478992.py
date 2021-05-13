# -*- coding: utf-8 -*-

mat = {}
vec = {}

n, m = map(int, raw_input().split())
for i in range(1, n+1):
    list = map(int, raw_input().split())
    for j in range(1, m+1):
        mat[(i, j)] = list[j-1]

for i in range(1, m+1):
    vec[i] = input()

for i in range(1, n+1):
    c = 0
    for j in range(1, m+1):
        c += mat[(i, j)]*vec[j]
    print c