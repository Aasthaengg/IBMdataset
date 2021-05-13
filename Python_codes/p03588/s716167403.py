#!/usr/bin/env python

n = int(input())
a = [0 for _ in range(n)]
b = [0 for _ in range(n)]
for i in range(n):
    a[i], b[i] = map(int, input().split())

ma = ima = 0 
for i in range(n):
    if a[i] >= ma: 
        ma = a[i]
        ima = i 

ans = a[ima]+b[ima]
print(ans)
