# -*- coding: utf-8 -*-
d, g = map(int,input().split())
p = [list(map(int, input().split())) for _ in range(d)]
# 点数の大きい順にソート
p.reverse()

ans = float('inf')

for i in range(1 << d):
    total = 0
    count = 0
    # ボーナスあり
    for j in range(d):
        if (i >> j) & 1:
            total += 100*(d-j)*p[j][0] + p[j][1]
            count += p[j][0]
    if total >= g:
        ans = min(ans, count)
        continue
    # ボーナスなし
    for j in range(d):
        if not (i >> j) & 1:
            for k in range(p[j][0]):
                total += 100*(d-j)
                count += 1
                if total >= g:
                    ans = min(ans, count)
                    break
            break

print(ans)
