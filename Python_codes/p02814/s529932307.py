import sys
from collections import defaultdict
from queue import deque
readline = sys.stdin.buffer.readline
#sys.setrecursionlimit(10**8)

from fractions import gcd


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    n, m = geta(int)
    a = tuple(geta(int))

    g = a[0] // 2

    def fn(i):
        ret = 0
        while i & 1 == 0:
            ret += 1
            i = i >> 1
        return ret

    t = fn(g)

    for ai in a[1:]:
        ai2 = ai // 2

        if t != fn(ai2):
            print(0)
            exit()

        g = (g * ai2) // gcd(g, ai2)

    print((m + g) // (g * 2))


if __name__ == "__main__":
    main()