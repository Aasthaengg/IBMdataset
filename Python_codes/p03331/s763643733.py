#!/usr/bin/env python

n = int(input())

def sumdigits(n):
    ret = 0 
    s = list(str(n))
    for i in range(len(s)):
        ret += int(s[i])
    return ret 

a = 1 
ans = 1000000
while n-a > 0:
    tmp = sumdigits(a) + sumdigits(n-a)
    if ans >= tmp:
        ans = tmp 
    a += 1

print(ans)
