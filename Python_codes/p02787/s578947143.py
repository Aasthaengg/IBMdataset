#!/usr/bin/env python3

def main():
    H, N = map(int, input().split())
    A = [None] * N
    B = [None] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    #1次元DPに書き換え
    INF = 10**12
    dp = [INF] * (H+1)
    dp[0] = 0
    for i in range(N):
        for j in range(H+1):
            dp[min(j+A[i],H)] = min(dp[min(j+A[i],H)],dp[j]+B[i])
    print(dp[H])

if __name__ == "__main__":
    main()
