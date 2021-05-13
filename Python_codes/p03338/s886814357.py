#!/usr/bin/env python3
n=int(input())
s=input()
ans = 0
for i in range(1,n):
    a = {j for j in s[:i]}
    b = {j for j in s[i:]}
    ans = max(ans, len(a & b))
print(ans)
