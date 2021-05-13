import math
import sys
import collections
import bisect


def main():
    n = int(input())
    c = collections.Counter(list(input()))
    b, r = c["B"], c["R"]
    print("Yes" if r > b else "No")


if __name__ == '__main__':
    main()
