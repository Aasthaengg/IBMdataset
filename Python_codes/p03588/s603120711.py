#!/usr/bin/env python3
n = int(input())
a = [0]*n
b = [0]*n
for i in range(n):
    a[i],b[i] = map(int,input().split())
a,b = zip(*sorted(zip(a,b)))
print(a[-1]+b[-1])