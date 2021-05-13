import sys
input = sys.stdin.readline
from collections import deque


def read():
    R, G, B, N = map(int, input().strip().split())
    return R, G, B, N


def solve(R, G, B, N):
    count = 0
    for r in range(N+1):
        for g in range(N+1):
            x = N - R * r - G * g
            if x >= 0 and x % B == 0:
                count += 1
    return count


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
