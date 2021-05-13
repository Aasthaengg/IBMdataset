#!/usr/bin/python3
# -*- coding: utf-8 -*-
n, k = map(int, input().split())
s_list = []
a_list = [0] * (n + 1)
b_list = [0] * (n + 1)
a_list[1] = 1
b_list[1] = 1
for i in range(k):
    l, r = map(int, input().split())
    s_list.append([l, r + 1])

for i in range(2, n + 1):
    for l, r in s_list:
        t2 = max(0, i - l)
        t1 = max(0, i - r)
        a_list[i] += b_list[t2] - b_list[t1]
    b_list[i] = (b_list[i - 1] + a_list[i]) % 998244353

print(a_list[n] % 998244353)

