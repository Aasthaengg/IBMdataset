import sys
import math


def input():
    return sys.stdin.readline().rstrip()


def main():
    mod =10**9+7
    N,M = map(int,input().split())
    A =[]
    for _ in range(M):
        a = int(input())
        A.append(a)

    dp= [0]*(N+1)
    ds= [0]*(N+1)
    for j in A:
        ds[j] =1

    dp[0] =1
    if ds[1] ==0:
        dp[1] =1
    for i in range(2,N+1):
        if ds[i] ==1:
            continue
        dp[i] = dp[i-1]+dp[i-2]
        dp[i] %=mod
    print(dp[N])





if __name__ == "__main__":
    main()
