def resolve():
    import sys
    
    readline = sys.stdin.readline

    N, K = map(int, readline().split())
    h = [int(x) for x in readline().split()]

    inf = float('inf')
    dp = [inf] * N
    dp[0] = 0

    for i in range(1, N):
        leng = i + 1 if i < K else K + 1
        for j in range(leng):
            cal = dp[i - j] + abs(h[i] - h[i - j])
            if dp[i] > cal:
                dp[i] = cal

    print(dp[-1])
            

resolve()
