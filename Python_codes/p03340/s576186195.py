#!/usr/bin/env python3
#ABC98 D

import sys
input = sys.stdin.readline
def d():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    l = 0
    r = 0
    s = 0
    while l < n and r < n:
        while s&a[r] == 0:
            s += a[r]
            r += 1
            ans += r-l
            if r == n:
                break
        if l==r:
            s += a[r]
            r += 1
        s -= a[l]
        l += 1
    print(ans)

if __name__ == '__main__':
    d()
