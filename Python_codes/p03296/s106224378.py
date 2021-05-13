#!/usr/bin/env python

n = int(input())
a = list(map(int, input().split()))

s = []
tmp = 1 
for i in range(n-1):
    if a[i] == a[i+1]:
        tmp += 1
        if i == n-2:
            s.append(tmp)
    else:
        if tmp != 1:
            s.append(tmp)
        tmp = 1 

ans = 0 
for i in s:
    ans += i//2

print(ans)
