import math
import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    A = set([int(input()) for _ in range(M)])
    dp = [0] * (N + 1)
    dp[0] = 1
    if 1 not in A:
        dp[1] = 1
    mod = 10 ** 9 + 7
    for i in range(2, N + 1):
        if i in A:
            dp[i] = 0
        else:
            dp[i] = (dp[i-2] + dp[i-1]) % mod
    print(dp[-1])


if __name__ == '__main__':
    main()
