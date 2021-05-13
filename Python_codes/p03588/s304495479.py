# -*- coding: utf-8 -*-
n = int(input())
ab = []
for i in range(n):
    ab.append([int(i) for i in input().split()])

ab.sort()
ans = ab[n-1][0] + ab[n-1][1]
print(ans)
