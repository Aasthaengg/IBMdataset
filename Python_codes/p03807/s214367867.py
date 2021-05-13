#!/usr/bin/env python3
n = int(input())
a = list(map(int, input().split()))
g = 0
k = 0

for i in a:
    if i % 2 == 1:
        k += 1

if k % 2 == 0:
    print("YES")
else:
    print("NO")
