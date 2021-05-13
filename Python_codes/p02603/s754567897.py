#!/usr/bin/env python
n = int(input())
a = list(map(int, input().split()))

money = 1000
kabu = 0 

for i in range(n-1):
    s = a[i]
    t = a[i+1]
    if s < t:
        k = money//s
        money %= s
        money += k*t 

print(money)
