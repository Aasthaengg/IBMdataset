#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    P = list(map(float, input().split()))

    dp = [0.0]*(N//2+2)
    dp[0] = 1.0
    for i in range(N):
        dp_ = [0.0]*(N+1)
        dp_[N//2+1]=dp[N//2+1]
        for j in range(min(i+1,N//2+1),-1,-1):
            dp_[j]+=dp[j-1]*P[i]
            dp_[j-1]+=dp[j-1]*(1-P[i])
        dp=dp_.copy()
    print(dp[N//2+1])

if __name__ == '__main__':
    main()