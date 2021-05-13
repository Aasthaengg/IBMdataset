import math
import collections
import bisect
from copy import copy


def main():
    N = int(input())

    ans = 0
    for i in range(1, N + 1):
        l = N // i
        ans += int(l * (l + 1) / 2) * i

    print(ans)


if __name__ == '__main__':
    main()
