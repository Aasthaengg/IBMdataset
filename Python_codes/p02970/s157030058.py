import sys
import math
import bisect


def main():
    n, d = map(int, input().split())
    d = 2 * d + 1
    ans = (n + d - 1) // d
    print(ans)

if __name__ == "__main__":
    main()
