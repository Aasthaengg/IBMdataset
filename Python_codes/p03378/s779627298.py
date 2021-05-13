import sys
from bisect import bisect_left
def input(): return sys.stdin.readline().strip()


def main():
    n, m, x = map(int, input().split())
    A = list(map(int, input().split()))
    idx = bisect_left(A, x)
    print(min(idx, m - idx))


if __name__ == "__main__":
    main()
