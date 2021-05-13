#!/usr/bin/env python

n, x = map(int, input().split())
a = list(map(int, input().split()))

a = sorted(a)
if x < a[0]:
    print(0)
    exit()

cnt = 0 
al = False
for i in range(n):
    if x >= a[i]:
        x -= a[i]
        cnt += 1
    else:
        break
    if i == n-1:
        al = True

if al: 
    if x > 0:
        ans = cnt-1
    else:
        ans = cnt 
else:
    ans = cnt 

print(ans)
