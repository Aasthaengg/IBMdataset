#!/usr/bin/env python3
n = int(input())
a = list(map(int, input().split()))
soko = a[0]
urine = 0
ans = 1000
for i in range(len(a) - 1):
    if a[i] < a[i + 1]:
        ans += (ans // a[i]) * (a[i + 1] - a[i])
    #print(ans)
print(ans)
