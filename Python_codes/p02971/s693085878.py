# -*- coding: utf-8 -*-
n = int(input())

a = [int(input()) for _ in range(n)]

most = max(a)
most_idx = a.index(most)
second = max(a[:most_idx] + a[most_idx+1:])

for i in range(n):
    print(second if a[i] == most else most)
