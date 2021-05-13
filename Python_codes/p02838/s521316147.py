import sys
from collections import deque
import itertools


def input():
    return sys.stdin.readline().rstrip()


def main():
    mod = 10 ** 9 + 7
    N = int(input())
    A = list(map(int, input().split()))
    l = [0] * 62
    n = [0] * 62
    for i in A:
        di = 0
        while i:
            if i % 2 == 1:
                l[di] += 1
            else:
                n[di] += 1
            i = i // 2
            di += 1
    di = 1
    ans = 0
    for j in range(61):
        ans += l[j] * (N - l[j]) * di

        di *= 2
        ans %= mod
    ans %= mod
    print(ans)


if __name__ == "__main__":
    main()
