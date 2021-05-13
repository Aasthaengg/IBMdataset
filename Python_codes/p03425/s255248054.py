#!/usr/bin/env python3

n = int(input())
s = [input() for _ in range(n)]
d = {}

for c in s:
    if c[0] not in d:
        d[c[0]] = 1 
    else:
        d[c[0]] += 1

tmp = d.copy()
t = ['M', 'A', 'R', 'C', 'H']
for c in tmp:
    if c not in t:
        d.pop(c)

ans = 0 
dlist = list(d.items())
for i in range(len(dlist)):
    for j in range(i+1, len(dlist)):
        for k in range(j+1, len(dlist)):
            ans += dlist[i][1]*dlist[j][1]*dlist[k][1]
print(ans)
