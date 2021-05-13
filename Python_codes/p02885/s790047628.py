import sys
import math
import bisect


def main():
    n, m = map(int, input().split())
    n = max(0, n - 2 * m)
    print(n)

if __name__ == "__main__":
    main()
