#!/usr/bin/env python3

N, K = map(int, input().split())
num = {}
cnt = 0
for i in range(N):
    a, b = map(int, input().split())
    if a in num: num[a] += b
    else: num[a] = b

for k, v in sorted(num.items()):
    cnt += v
    if K <= cnt:
        print(k)
        exit()
