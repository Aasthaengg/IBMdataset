#!/usr/bin/python
# -*- coding:utf-8 -*-

n = int(input())
S = list(map(int, input().split(" ")))
q = int(input())
T = list(map(int, input().split(" ")))

num = 0
for t in T:
    if t in S:
        num += 1
print(num)