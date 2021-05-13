import sys
from itertools import combinations
import bisect


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i, j in combinations(l, 2):
        lb = abs(j - i)
        ub = i + j
        ans += bisect.bisect_left(l, ub) - bisect.bisect_right(l, lb)
        for e in (i, j):
            if e > lb:
                ans -= 1

    print(ans // 3)


if __name__ == "__main__":
    main()
