import sys
from collections import Counter

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    n = in_n()
    v = in_nl()
    c1 = Counter(v[::2]).most_common()
    c2 = Counter(v[1::2]).most_common()
    if c1[0][0] == c2[0][0]:
        if len(c1) == 1 and len(c2) == 1:
            count = n // 2
        elif len(c1) == 1:
            count = n // 2 + c2[1][1]
        elif len(c2) == 1:
            count = n // 2 + c1[1][1]
        else:
            count = max(c1[0][1] + c2[1][1], c1[1][1] + c2[0][1])
    else:
        count = c1[0][1] + c2[0][1]
    print(n - count)


if __name__ == '__main__':
    main()
