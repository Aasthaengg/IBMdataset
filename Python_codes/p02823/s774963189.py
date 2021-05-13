import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
#sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    n, a, b = geta(int)

    if (b - a) & 1 == 0:
        print((b - a) // 2)
    else:
        print(min((a + b - 1) // 2, n - (a + b - 1) // 2))


if __name__ == "__main__":
    main()