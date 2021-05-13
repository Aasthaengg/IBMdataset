# -*- coding: utf-8 -*-
n = int(input())
p = list(map(int, input().split()))

miss_cnt = 0

for i in range(1, n+1):
    if p[i-1] != i:
        miss_cnt += 1

print('YES' if miss_cnt <= 2 else 'NO')
