#!/usr/bin python3
# -*- coding: utf-8 -*-

from bisect import bisect_left, bisect_right

def main():
    N,C,K = map(int, input().split())
    Ti = list(int(input()) for _ in range(N))
    Ti.sort()
    i = 0
    ret = 0
    while i<N:
        ret += 1
        s = i
        Ts = Ti[i]
        while i<N and Ti[i]<=(Ts+K) and (i-s)<C:
            i += 1

    print(ret)

if __name__ == '__main__':
    main()