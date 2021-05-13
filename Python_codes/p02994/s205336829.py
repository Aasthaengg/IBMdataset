#!/usr/bin/env python3
n, k = map(int, input().split())
if k > 0:
    print(k*(n-1)+n*(n-1)//2)
elif k > -n:
    print(k*n+n*(n-1)//2)
else:
    print(k*(n-1)+(n-1)*(n-2)//2)
