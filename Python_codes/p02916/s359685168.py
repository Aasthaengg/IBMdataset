# -*- coding: utf-8 -*-

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = b[a[0]-1]

for i, food in enumerate(a[1:]):
    ans += b[food-1]
    if a[i] == food-1:
        ans += c[food-2]

print(ans)
