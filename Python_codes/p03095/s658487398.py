#!/usr/bin python3
# -*- coding: utf-8 -*-

from collections import Counter

def main():
    mod = 10**9+7
    N = int(input())
    S = list(input())
    S = Counter(S)
    ret = 1
    for i,c in S.items():
        ret *= (c+1)
        ret %= mod
    print((ret-1)%mod)

if __name__ == '__main__':
    main()