#!/usr/bin/env python3

X = int(input())
N = 100000
k = 1
for i in range(N):
    if k*100 <= X <= k*105:
        print(1)
        exit()
    k += 1
print(0)
