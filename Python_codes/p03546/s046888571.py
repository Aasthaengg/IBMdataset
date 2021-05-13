#!/usr/bin/env python3
import copy

H, W = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
grid = [list(map(int, input().split())) for _ in range(H)]

d = dict()
nums = [i for i in range(10) if i != 1]
d["-1_1"] = 0

q = [[[1], 0]]

while q:
    tmp = q.pop()
    num, cost = tmp[0], tmp[1]
    key = str(num[-1]) + "_1"
    if d.get(key):
        d[key] = min(d[key], cost)
    else:
        d[key] = cost
    if len(num) < 10:
        for n in nums:
            num_tmp = copy.copy(num)
            if n not in set(num_tmp):
                num_tmp.append(n)
                q.append([num_tmp, cost + c[num_tmp[-1]][num_tmp[-2]]])

ans = 0
for i in range(H):
    for j in range(W):
        tmp = grid[i - 1][j - 1] 
        ans += d[str(tmp) + "_1"]
print(ans)