#!/usr/bin/env python

n, x = map(int, input().split())
a = list(map(int, input().split()))

a = sorted(a)
if x < a[0]:
    print(0)
    exit()

if sum(a) < x:
    print(n-1)
    exit()

cnt = 0 
for i in range(n):
    if x >= a[i]:
        x -= a[i]
        cnt += 1

ans = cnt 
print(ans)
