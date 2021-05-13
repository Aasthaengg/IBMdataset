import sys


def resolve():
    readline = sys.stdin.readline

    N, K = map(int, readline().split())
    P = [int(x) for x in readline().split()]

    P = sorted(P)

    print(sum(P[:K]))

resolve()
