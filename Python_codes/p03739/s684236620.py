import sys
import numpy as np
import copy

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    A = list(map(int, input().split()))

    # + - + - の順番
    S = 0
    cnt = 0
    for i in range(N):
        S += A[i]
        if i % 2 == 0:
            # +
            if S > 0:
                continue
            else:
                cnt += abs(S) + 1
                S += abs(S) + 1
        else:
            # -
            if S < 0:
                pass
            else:
                cnt += abs(S) + 1
                S -= abs(S) + 1
    ans = cnt

    # - + - +の順番
    S = 0
    cnt = 0
    for i in range(N):
        S += A[i]
        if i % 2 == 1:
            # +
            if S > 0:
                continue
            else:
                cnt += abs(S) + 1
                S += abs(S) + 1
        else:
            # -
            if S < 0:
                continue
            else:
                cnt += abs(S) + 1
                S -= abs(S) + 1

    if ans > cnt:
        ans = cnt
    print(ans)


if __name__ == "__main__":
    main()
