#!/usr/bin/env python

n = int(input())
a = list(map(int, input().split()))
d = [0 for _ in range(n-1)]
for i in range(n-1):
    d[i] = a[i+1]-a[i]

ans = 1 
flg = [False, False]

for i in range(n-1):
    if d[i] > 0:
        flg[0] = True
    elif d[i] < 0:
        flg[1] = True

    if flg[0] == flg[1] == True:
        ans += 1
        flg = [False, False]

print(ans)
