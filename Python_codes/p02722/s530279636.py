#!/usr/bin python3
# -*- coding: utf-8 -*-

import sys
input = sys.stdin.readline
def make_divisors(n):
    divisors = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

def main():
    N=int(input())
    ret=0
    if N==2:
        ret=1
    else:
        div=make_divisors(N)
        div=div+make_divisors(N-1)
        div.append(N)
        div.append(N-1)
        for k in div:
            n=N
            while n%k==0:
                n=n//k
            ret += n%k==1
        if N==2:
            ret = 1
    print(ret)

if __name__ == '__main__':
    main()