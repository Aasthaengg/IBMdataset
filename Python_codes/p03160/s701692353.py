import math


def chmax(a, b):
    if a >= b:
        return a
    return b


def chmin(a, b):
    if a <= b:
        return a
    return b


def main():
    nn = int(input())
    hh = list(map(int, input().split()))

    dp = [math.inf]*nn
    dp[0] = 0
    dp[1] = chmin(dp[1],dp[0]+abs(hh[1]-hh[0]))
    for i in range(2,nn):
        dp[i] = chmin(dp[i],dp[i-1]+abs(hh[i]-hh[i-1]))
        dp[i] = chmin(dp[i],dp[i-2]+abs(hh[i]-hh[i-2]))

    print(dp[nn-1])


main()
