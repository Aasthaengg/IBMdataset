#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    n = int(input())
    mod = pow(10,9) + 7
    ans = pow(10,n,mod)
    ans -= pow(9,n,mod)*2
    ans += pow(8,n,mod)

    print(ans%mod)

if __name__ == '__main__':
    main()
