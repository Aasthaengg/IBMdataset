import math
import sys
from collections import Counter
import bisect
readline = sys.stdin.readline


def main():
    cnt = 0
    n = int(readline().rstrip())
    L = sorted(list(map(int, readline().rstrip().split())))
    for a in range(0, n - 2):
        for b in range(a + 1, n - 1):
            k = L[a] + L[b]
            index = bisect.bisect_left(L, k)
            cnt += index - b - 1
    print(cnt)


if __name__ == '__main__':
    main()
