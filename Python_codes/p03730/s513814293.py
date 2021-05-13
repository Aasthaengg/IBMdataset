#!/usr/bin/env python3

A,B,C = [int(i) for i in input().split()]

M = []
for i in range(1,100+1):
    if (A*i)%B in M:
        break
    else:
        M.append((A*i)%B)

if C in M:
    print("YES")
else:
    print("NO")
