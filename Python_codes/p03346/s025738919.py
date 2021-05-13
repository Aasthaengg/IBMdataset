#!usr/bin/env python3
n = int(input())
p = [int(input()) for i in range(n)]
f = [0]*(n+1)
m = [n-1]*(n+1)
for i in p:
    if f[i-1]:
        m[i] = m[i-1]-1
    f[i] = 1
print(min(m))
