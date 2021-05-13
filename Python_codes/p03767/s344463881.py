# -*- coding: utf-8 -*-

N = int(input())
a = sorted(list(map(int, input().split())))

ans = 0
for i in range(0, 2*N, 2):
    ans += a[i+N]

print(ans)
