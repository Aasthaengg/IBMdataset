#!/usr/bin/env python3

n = int(input())
s = [input() for _ in range(n)]

c = [0 for _ in range(5)]
t = 'MARCH'

for i in range(n):
    for j in range(5):
        if s[i][0] == t[j]:
            c[j] += 1
ans = 0 
for i in range(5):
    for j in range(i+1, 5): 
        for k in range(j+1, 5): 
            ans += c[i]*c[k]*c[j]
print(ans)
