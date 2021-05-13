#!/usr/bin/env python3
n = int(input())
s = [[*map(int, input().split())] for i in range(n)]
s.sort(key=lambda x: x[1])
c = 0
for a, b in s:
    c += a
    if c > b:
        print("No")
        exit()
print("Yes")
