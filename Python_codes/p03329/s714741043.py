#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    INF = 10**10
    dp = [INF] * (N+1)
    dp[0] = 0
    bk = set([1])
    for i in range(100):
        if pow(6,i)>N:
            break
        bk.add(pow(6,i))
    for i in range(100):
        if pow(9,i)>N:
            break
        bk.add(pow(9,i))

    for i in range(N):
        for j in bk:
            if (i+j)<=N:
                dp[i+j] = min(dp[i+j], dp[i]+1)
    print(dp[N])

if __name__ == '__main__':
    main()