import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
#sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    N = gete(int)
    A = tuple(geta(int))

    ans = sum([1 / ai for ai in A])

    print(1 / ans)


if __name__ == "__main__":
    main()