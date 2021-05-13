#!/usr/bin/env python3
n, k = map(int, input().split())
h = list(map(int, input().split()))
a = 0
for i in h:
    a += i >= k
print(a)