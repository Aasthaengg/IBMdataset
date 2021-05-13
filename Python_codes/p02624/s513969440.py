import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    N = int(readline().rstrip())
    ans = 0
    for i in range(1, N+1):
        n = N // i
        ans += 0.5 * n * (2*i + i * (n-1))
    print(int(ans))


if __name__ == '__main__':
    main()
