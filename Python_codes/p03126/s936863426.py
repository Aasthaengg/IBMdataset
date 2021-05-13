#!/usr/bin/env python3
n, m = map(int, input().split())
ans = set(x for x in range(1, m+1))
for i in range(n):
    k, *a = map(int, input().split())
    ans = set(a) & ans
print(len(ans))
