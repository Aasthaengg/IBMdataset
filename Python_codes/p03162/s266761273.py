def resolve():
    import sys
    import itertools
    import numpy as np

    readline = sys.stdin.readline

    N = int(readline())
    lst = [list(map(int, readline().split())) for _ in [0] * N]

    dp = np.full((N, 3), -1, np.int32)
    for i in range(N):
        for a, b in itertools.permutations([0, 1, 2], 2):
            if a == b:
                continue
            if i == 0:
                dp[i][a] = lst[i][a]
            else:
                dp[i][a] = max(dp[i][a], dp[i - 1][b] + lst[i][a])
    print(max(dp[-1]))

resolve()
