#!/usr/bin/env python3
n = int(input())
b = list(map(int, input().split()))
b.insert(0, 1000000)
b.append(10000000)
a = 0
for i in range(n):
    a += min(b[i], b[i+1])
print(a)