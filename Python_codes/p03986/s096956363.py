import sys
import itertools

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    S = list(in_s())[::-1]
    N = len(S)

    gr = itertools.groupby(S)

    count = 0
    tnum = 0
    for k, v in gr:
        num = sum(1 for _ in v)
        if k == 'S':
            count += min(tnum, num)
            tnum -= min(tnum, num)
        else:
            tnum += num

    # print(count)

    ans = N - count * 2
    print(ans)


if __name__ == '__main__':
    main()
