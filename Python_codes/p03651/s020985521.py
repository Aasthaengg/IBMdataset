#!/usr/bin python3
# -*- coding: utf-8 -*-

from fractions import gcd   #for python3.4
from math import gcd        #for python3.8

def Gcd(lt):
    l = len(lt)
    ret = [1]*l
    ret[0] = lt[0]
    for i in range(1,l):
        ret[i] = gcd(ret[i-1], lt[i])
    return ret

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    g = Gcd(A)[-1]
    if K<=max(A) and K%g==0:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')

if __name__ == '__main__':
    main()