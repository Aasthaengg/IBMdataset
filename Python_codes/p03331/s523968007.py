import sys
import collections
import bisect
import math
import time


def main():
    n = input()
    if len(n) == 1:
        print(int(n))
        return

    if len(n) - list(n).count("0") >= 2:
        print(sum(list(map(lambda x: int(x), list(n)))))
        return

    if n[0:2] == "10":
        print(10)
        return

    print(n[0])


if __name__ == '__main__':
    main()
