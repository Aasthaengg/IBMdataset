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
    N, M = in_nn()
    t = in_na()
    PY = list(zip(t, t))

    d = defaultdict(list)

    for i in range(M):
        p, y = PY[i]
        d[p].append(y)

    ans = dict()
    for k, v in d.items():
        v.sort()
        for i, y in enumerate(v):
            ans[(k, y)] = '{:0>6}{:0>6}'.format(k, i + 1)

    for i in range(M):
        p, y = PY[i]
        print(ans[(p, y)])


if __name__ == '__main__':
    main()
