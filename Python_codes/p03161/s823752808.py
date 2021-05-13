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
    nn,kk = list(map(int,input().split()))
    hh = list(map(int, input().split()))

    dp = [math.inf]*nn
    dp[0] = 0
    for i in range(1,nn):
        gg = min(i,kk)
        for j in range(1,gg+1):
            dp[i] = chmin(dp[i],dp[i-j]+abs(hh[i]-hh[i-j]))

    print(dp[nn-1])


main()
