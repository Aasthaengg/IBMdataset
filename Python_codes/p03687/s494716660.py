import sys
import itertools
import copy

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    s = list(in_s())[::-1]
    ss = sorted(list(set(s)))

    ans = 100
    for c in ss:
        count = 0
        ts = [c if t == c else 'A' for t in s]
        gr = itertools.groupby(ts)
        for k, v in gr:
            n = len(list(v))
            if k != c:
                count = max(count, n)
        ans = min(ans, count)

    print(ans)


if __name__ == '__main__':
    main()
