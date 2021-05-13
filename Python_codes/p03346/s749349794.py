import sys
import itertools

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

    N = in_n()
    P = list(in_all())
    Q = [0] * (N + 1)

    if N == 1:
        print(0)
        exit()

    for i in range(N):
        Q[P[i]] = i

    dc = []
    for i in range(1, N):
        if Q[i] < Q[i + 1]:
            dc.append(1)
        else:
            dc.append(0)

    gr = itertools.groupby(dc)

    cnt = 1
    for k, v in gr:
        v = sum(1 for _ in v)
        if k == 1:
            cnt = max(cnt, v + 1)

    print(N - cnt)


if __name__ == '__main__':
    main()
