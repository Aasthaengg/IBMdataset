#!/usr/bin/env python3

import sys

DEBUG = False

def read(t):
    return t(sys.stdin.readline().rstrip())


def read_list(t, sep = " "):
    return [t(s) for s in sys.stdin.readline().rstrip().split(sep)]


def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
    return


def main():
    n = read(int)
    s = read(str)

    ans = 0
    for i in range(1, len(s) - 1):
        x = s[0:i]
        y = s[i:]

        x_chrs = set(list(x))
        y_chrs = set(list(y))

        nr_dup_chrs = x_chrs & y_chrs
        if ans < len(nr_dup_chrs):
            ans = len(nr_dup_chrs)

    print(ans)

if __name__ == "__main__":
    main()
