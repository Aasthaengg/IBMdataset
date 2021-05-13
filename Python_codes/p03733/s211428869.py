#!/usr/bin/env python3
n,t,*s=map(int,open(0).read().split())
ans=0
e=0
for i in s:
    if e > i:
        ans += t - e + i
    else:
        ans += t
    e = i + t
print(ans)
