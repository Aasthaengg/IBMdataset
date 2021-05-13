#!/usr/bin/env python3
def main():
    import numpy as np

    N = int(input())
    happiness = [list(map(int, input().split())) for _ in range(N)]

    dp = np.zeros((N, 3), dtype=np.int64)
    dp[0] = happiness[0]
    for i in range(1, N):
        for a, yesterday in enumerate(dp[i - 1]):
            for b, today in enumerate(happiness[i]):
                if a == b:
                    continue
                dp[i][b] = max(dp[i][b], yesterday + today)
    print(max(dp[-1]))


if __name__ == '__main__':
    main()
