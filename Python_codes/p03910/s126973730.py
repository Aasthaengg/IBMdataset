#!/usr/bin/env python3

N = int(input())

cnt = 0
for i in range(1, 10**7+1):
    cnt += i
    if cnt > N: break

z = cnt - N

for j in range(1, i+1):
    if j == z: continue
    print(j)
