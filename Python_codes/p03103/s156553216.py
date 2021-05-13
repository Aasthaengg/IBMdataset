#!/usr/bin/env python3

n, m = map(int, input().split())
a = [-1 for _ in range(n)]
b = [-1 for _ in range(n)]
d = {}
for i in range(n):
    a[i], b[i] = map(int, input().split())
    if a[i] not in d:
        d[a[i]] = b[i]
    else:
        d[a[i]] += b[i]

d = sorted(d.items(), key=lambda x:x[0])
num = ans = 0 
for i in range(len(d)):
    tmp = num 
    num += d[i][1]
    if num <= m:
        ans += d[i][0]*d[i][1]
    else:
        ans += d[i][0]*(m-tmp)
        break

print(ans)
