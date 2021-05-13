#!/usr/bin/env python3
n = int(input())
a = list(map(int,input().split()))
a.append(0)
total = 0
for i in range(n+1):
    total += abs(a[i] - a[i-1])
    #print(total,abs(a[i] - a[i-1]))
for i in range(-1,n-1):
    if (a[i+1]-a[i]) *(a[i+2]-a[i+1]) > 0:
        print(total) # 間に挟まれるなら 
    else: print(total - 2 * min(abs(a[i+1] -a[i]) ,abs(a[i+1] -a[i+2])))
