import sys
import collections
import bisect


def main():
    [n, a, b, c] = [input() for _ in range(4)]
    print(sum((len(set([a[i], b[i], c[i]]))-1) for i in range(int(n))))


if __name__ == '__main__':
    main()
