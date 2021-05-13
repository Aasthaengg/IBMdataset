import sys
import numpy as np
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N = int(readline())
    coin = [6**i for i in range(10) if 6**i <= N]
    coin += [9**i for i in range(10) if 9**i <= N]

    dp = np.zeros(N+1,dtype=np.int32)
    dp += MOD
    dp[0] = 0
    for c in coin:
        for _ in range(9):
            dp[c:] = np.minimum(dp[:-c]+1, dp[c:])
    print(dp[-1])


if __name__ == '__main__':
    main()