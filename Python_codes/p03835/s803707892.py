#!/usr/bin/env python3

K, S = map(int, input().split())
AB = []
ret = 0
for i in range(K+1):
    for j in range(K+1):
        AB.append(i+j)

for i in range(len(AB)):
    if 0 <= S - AB[i] <= K:
        ret += 1

print(ret)
