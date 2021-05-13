#!/usr/bin/env python3

X = int(input())

ret = 0
for i in range(1, 1001):
    for j in range(2, 20):
        if i**j <= X:
            ret = max(i**j, ret)

print(ret)

