#!/usr/bin python3
# -*- coding: utf-8 -*-

from fractions import gcd   #for python3.4
#from math import gcd        #for python3.8

def lcm(a,b):
    G = gcd(a, b) #最大公約数
    L = (a//G)*b #最小公倍数
    return L

def main():
    N, M = map(int, input().split())
    S = input()
    T = input()
    L = lcm(N,M)
    if S[::L//M]==T[::L//N]:
        print(L)
    else:
        print(-1)

if __name__ == '__main__':
    main()