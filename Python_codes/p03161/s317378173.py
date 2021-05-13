# coding=utf-8

if __name__ == '__main__':
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    inf = float('inf')

    dp = [inf] * N
    dp[0] = 0

    for i in range(N):
        for j in range(1, K+1):
            if i + j < N:
                if dp[i+j] > dp[i] + abs(h[i] - h[i+j]):
                    dp[i+j] = dp[i] + abs(h[i] - h[i+j])

    print(dp[N-1])
