def resolve():
    import sys
    import numpy as np

    read = sys.stdin.read
    readline = sys.stdin.readline

    N, K = map(int, readline().split())
    h = np.array(read().split(), np.int32)

    # 貰うDP
    inf = 10 ** 9
    dp = np.full(N, inf, np.int64)
    dp[0] = 0


    for i, e in enumerate(h[1:], 1):
        lb = max(0, i - K)
        dp[i] = np.min(dp[lb:i] + np.abs(h[lb:i] - e))

    print(dp[-1])

    
resolve()
