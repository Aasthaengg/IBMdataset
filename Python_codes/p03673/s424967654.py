#!/usr/bin/env python

n = int(input())
a = list(map(int, input().split()))
b = []

if n%2==1:
    i = n-1 
    while i>=0:
        b.append(a[i])
        i -= 2
    i = 1 
    while i<=n-2:
        b.append(a[i])
        i += 2
else:
    i = n-1 
    while i>=1:
        b.append(a[i])
        i -= 2
    i = 0 
    while i<=n-2:
        b.append(a[i])
        i += 2

b = list(map(str, b)) 
ans = ' '.join(b)
print(ans)
