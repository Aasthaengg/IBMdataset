#!/usr/bin/env python3
import sys 
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

d = {}
for i in range(n):
    d[i] = a[i]

d = sorted(d.items(), key=lambda x:x[1])
ans = ''
for i in range(n):
    ans += str((d[i][0]+1)) + ' ' 

print(ans)
