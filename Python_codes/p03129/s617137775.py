import math
import sys
import collections
import bisect


def main():
    n, k = map(int, input().split())
    print("YES" if (n + 1)//2 >= k else "NO")


if __name__ == '__main__':
    main()
