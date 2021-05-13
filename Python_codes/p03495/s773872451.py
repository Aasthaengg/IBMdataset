#!/usr/bin/env python3

n, k = map(int, input().split())
a = list(map(int, input().split()))

d = {}
for i in a:
    if i not in d:
        d[i] = 1 
    else:
        d[i] += 1

ans = 0 
d = sorted(d.items(), key=lambda x:x[1])
for i in range(len(d)-k):
   ans += d[i][1] 

print(ans)
