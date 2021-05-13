# -*- coding: utf-8 -*-

A = int(input()) # 500円
B = int(input()) # 100円
C = int(input()) # 50円
X = int(input()) # 金額

ans = 0
tmp_x = 0

for i in range(0, A + 1):
    for j in range(0, B + 1):
        for k in range(0, C + 1):
            tmp_x = (500 * i) + (100 * j) + (50 * k)
            if X == tmp_x:
                ans += 1

print(ans)