#!/usr/bin/env python

n = int(input())
s = input()
t = input()

ans = ''
for i in range(n+1):
    if s[n-i:] == t[:i]:
        ans = s + t[i:]

print(len(ans))
