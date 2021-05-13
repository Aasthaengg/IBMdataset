import sys
from collections import deque

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, X, Y = map(int, readline().split())

    X -= 1
    Y -= 1

    ans = [0] * N

    for i in range(N - 1):
        for j in range(i + 1, N):
            d = min(j - i, abs(i - X) + 1 + abs(Y - j), abs(j - X) + 1 + abs(X - i))
            ans[d] += 1

    print('\n'.join(map(str, ans[1:])))
    return


if __name__ == '__main__':
    main()
