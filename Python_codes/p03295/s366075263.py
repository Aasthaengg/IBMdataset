import sys
from collections import deque

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():

    N, M = in_nn()
    d = dict()

    for i in range(M):
        a, b = in_nn()
        if a in d:
            d[a] = min(d[a], b)
        else:
            d[a] = b

    edge = list(sorted(d.items(), key=lambda x: x[0], reverse=True))

    remove = deque()
    for a, b in edge:
        if remove:
            if b <= remove[0]:
                remove.appendleft(a)
        else:
            remove.appendleft(a)

    print(len(remove))


if __name__ == '__main__':
    main()
