import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    over = []
    for a in A:
        if a >= K:
            over.append(a)

    if len(over) == 0:
        print("IMPOSSIBLE")
        exit(0)
    if min(over) == K:
        print("POSSIBLE")
        exit(0)

    while True:
        min_A = min(A)
        B = []
        for a in A:
            r = a % min_A
            if r != 0:
                B.append(r)
        if len(B) == 0:
            print("IMPOSSIBLE")
            exit(0)
        else:
            min_B = min(B)
            for oa in over:
                if (oa - K) % min_B == 0:
                    print("POSSIBLE")
                    exit(0)
            A = A + B
