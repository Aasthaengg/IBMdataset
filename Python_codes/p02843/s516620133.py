#!/usr/bin/env python3
n = int(input())
a = n % 100
b = n//100
if b >= (a//5 + (a % 5 != 0)):
    print(1)
else:
    print(0)
