#!/usr/bin/env python

N, K = map(int, input().split())
ans = 0

for i in range(1, N+1):
    j, now = 0, i
    while now < K :
        j+=1
        now *= 2
    ans+= 2**(-j)

print(ans/N)
