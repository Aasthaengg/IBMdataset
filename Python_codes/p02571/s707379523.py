#!/usr/bin/env python

def count(a, b):
    ans = 0
    for i, j in zip(a, b):
        if i != j:
            ans += 1
    return ans

s = input()
t = input()

ans = len(s)

for i in range(0, len(s)-len(t)+1):
    a = s[i:i+len(t)+1]
    ans = min(ans, count(a, t))

print(ans)
