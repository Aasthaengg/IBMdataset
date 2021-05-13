#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    n, m, d = map(int, input().split())
    if d==0:
        K = n
    elif n>=2*d:
        K = 2*d + 2*(n-2*d)
    else:
        K = 2*(n-d)
    K/=n**2
    K*=m-1
    print(K)

if __name__ == '__main__':
    main()