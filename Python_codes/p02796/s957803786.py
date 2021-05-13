#!/usr/bin/env python3
n = int(input())
rl = [[0, 0]] * n
for i in range(n):
    x, l = map(int, input().split())
    rl[i] = [x + l, x - l]
rl.sort()
l = [0] * n
r = [0] * n
for i in range(n):
    r[i], l[i] = rl[i]
ans = 1
p = 0
for i in range(1, n):
    if r[p] <= l[i]:
        ans += 1
        p = i
print(ans)
