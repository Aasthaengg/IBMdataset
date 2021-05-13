import sys
from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():

    S = in_n()
    M = 10**9
    x1, y1 = 0, 0
    x2, y2 = M, 1
    q, r = divmod(S, M)
    if r == 0:
        x3, y3 = r, q
    else:
        x3, y3 = M - r, q + 1

    #print(x2 * y3 - y2 * x3)
    print(x1, y1, x2, y2, x3, y3)


if __name__ == '__main__':
    main()
