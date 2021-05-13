import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
#sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    n, k, s = geta(int)

    r = s + 1 if s < 10**9 else 1

    ans = [s] * k + [r] * (n - k)
    print(*ans, sep=" ")


if __name__ == "__main__":
    main()