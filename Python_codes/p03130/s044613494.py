import sys
import collections
import bisect


def main():
    k = [list(map(int, input().split())) for _ in range(3)]

    c = collections.Counter(k[0] + k[1] + k[2])
    print('YES' if sorted(c.values()) == [1, 1, 2, 2] else 'NO')


if __name__ == '__main__':
    main()
