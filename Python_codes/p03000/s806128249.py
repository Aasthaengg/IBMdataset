#!/usr/bin/env python3
n, x, *l = map(int, open(0).read().split())
a = n+1
i=sum(l)
while a > 1 and i>x:
    a -= 1
    i-=l[a-1]
print(a)
