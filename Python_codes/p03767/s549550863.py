# -*- coding: utf-8 -*-
n = int(input())
a = [int(i) for i in input().split()]

ans = 0
a.sort(reverse = True)
for i in range(1, 2*n+1, 2):
    #print(i, a[i])
    ans += a[i]
print(ans)
