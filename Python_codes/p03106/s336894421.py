# author:  Taichicchi
# created: 10.09.2020 08:12:15

import sys

A, B, K = map(int, input().split())

cnt = 0

ls = []

for k in range(1, max(A, B) + 1):
    if (A % k == 0) & (B % k == 0):
        cnt += 1
        ls.append(k)

print(ls[-K])