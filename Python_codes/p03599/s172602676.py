import sys
import bisect
from fractions import Fraction

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


def main():

    A, B, C, D, E, F = in_nn()

    water = set()
    for i in range(31):
        for j in range(31):
            t = i * A * 100 + j * B * 100
            if t <= F:
                water.add(t)
            else:
                break
    water = list(sorted(water))

    sugar = set()
    for i in range(3001):
        for j in range(3001):
            t = i * C + j * D
            if t <= F:
                sugar.add(t)
            else:
                break
    sugar = list(sorted(sugar))

    max_f = 0
    ans = (100 * A, 0)
    for w in water:
        for s in sugar:
            if w + s <= F and s <= (w // 100) * E and w + s != 0:
                if max_f < Fraction(s, w + s):
                    max_f = Fraction(s, w + s)
                    ans = (s + w, s)

    print(ans[0], ans[1])


if __name__ == '__main__':
    main()
