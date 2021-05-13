#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
c = 1
for i in a:
    if i == c:
        c += 1
print(-1*(c==1) or n - c + 1)
