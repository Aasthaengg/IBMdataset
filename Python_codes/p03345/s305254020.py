#!/usr/bin/env python3

A,B,C,K = [int(x) for x in input().split(" ")]

if K % 2 == 0:
    ans = A - B
else:
    ans = B - A

print(ans)
