#!/usr/bin/env python3
n = int(input())
s = [input() for i in range(n)]
m = int(input())
t = [input() for i in range(m)]

ans = 0
for i in s:
    sc = s.count(i)
    tc = t.count(i)
    cnt = sc - tc
    if cnt > ans:
        ans = cnt

print(ans)