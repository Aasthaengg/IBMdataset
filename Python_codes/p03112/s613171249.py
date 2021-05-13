#!/usr/bin python3
# -*- coding: utf-8 -*-

from bisect import bisect_left, bisect_right

def main():
    A, B, Q = map(int, input().split())
    a = [int(input()) for _ in range(A)]
    b = [int(input()) for _ in range(B)]
    q = [int(input()) for _ in range(Q)]
    INF = 2*10**10
    a = [-INF] + a + [INF]
    b = [-INF] + b + [INF]

    for x in q:
        ai = bisect_left(a, x)
        ap = a[ai]-x
        am = x-a[ai-1]
        bi = bisect_left(b, x)
        bp = b[bi]-x
        bm = x-b[bi-1]

        ret = INF
        if max(ap,bp)<INF:
            ret = min(ret, max(ap, bp))
        if max(am,bm)<INF:
            ret = min(ret, max(am, bm))
        ret = min(ret, ap+2*bm, am+2*bp, bp+2*am, bm+2*ap)
        print(ret)

if __name__ == '__main__':
    main()