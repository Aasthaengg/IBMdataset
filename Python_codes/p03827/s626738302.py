#!/usr/bin/env python3
N = int(input())
S = input()

l = [0]
x = 0
for i in S:
    if i == 'I':
        x += 1
    else:
        x -= 1
    l.append(x)
print(max(l))
