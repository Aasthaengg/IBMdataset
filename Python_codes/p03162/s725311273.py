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
    arr = [list(map(int, input().split())) for l in range(nn)]
    dp = [[0] * 3 for i in range(nn+1)]

    for i in range(nn):
        for j in range(3):
            for k in range(3):
                if j == k:
                    continue
                dp[i+1][j] = chmax(dp[i+1][j],dp[i][k]+arr[i][k])

    print(max(dp[nn][0],dp[nn][1],dp[nn][2]))


main()