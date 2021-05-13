#!/usr/bin/env python3
#diverta C

N = int(input())
a = list(map(int,input().split()))
a.sort()
s = a[0]
l = a[-1]
log = []
for i in a[1:-1]:
    if i > 0:
        log += [(s, i)]
        s -= i
    else:
        log += [(l, i)]
        l -= i
log += [(l, s)]
print(l - s)
for i, j in log:
    print(i, j)