#!/usr/bin python3
# -*- coding: utf-8 -*-

k = int(input())
a = list(map(int, input().split()))
a= a[::-1]
if a[0]!=2:
    print(-1)
    exit()
mi = a[0]
mx = a[0]*2-1
for i in range(1,k):
    ai = a[i]
    mi = (mi+ai-1)//ai
    mx = mx//ai
    if mi>mx:
        print(-1)
        exit()
    else:
        mi = mi*ai
        mx = (mx+1)*ai-1
print(mi, mx)