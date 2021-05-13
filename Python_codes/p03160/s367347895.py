# coding=utf-8

if __name__ == '__main__':

    N = int(input())
    h = list(map(int, input().split()))

    dp = [0] * 100100

    #print(dp)

    for i in range(N):
        if i == 0:
            continue
        if i == 1:
            dp[i] = abs(h[i-1] -h[i])
            continue
        
        if dp[i -2] + abs(h[i - 2] - h[i]) <= dp[i - 1] + abs(h[i - 1] - h[i]):
            dp[i] = dp[i -2] + abs(h[i - 2] - h[i])
            #print('a')

        else:
            dp[i] = dp[i - 1] + abs(h[i - 1] - h[i])
            #print('b')

    print(dp[N - 1])
    #print(dp)