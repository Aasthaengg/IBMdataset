#!/usr/bin/env python

h = int(input())

ans = 0 
n = 1 
while n <= h:
    ans += n
    n *= 2

print(ans)
