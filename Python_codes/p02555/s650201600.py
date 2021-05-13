#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    s = int(input())
    mod = pow(10,9) + 7

    dp = [0]*(s+1)
    dp[0] = 1
    for i in range(2,s+1):
        for j in range(0, (i-3)+1):
            dp[i] += dp[j]

    print(dp[s]%mod)
    

if __name__ == '__main__':
    main()
