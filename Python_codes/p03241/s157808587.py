#!/usr/bin/env python3
n, m = map(int, input().split())
for i in reversed(range(1,m//n+1)):
    if m%i<1:
        print(i)
        exit()
