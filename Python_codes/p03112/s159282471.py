#!/usr/bin/env python3

import bisect

def main():
    a, b, q = map(int, input().split())
    huge = 10 ** 18
    s = [-huge] + [int(input()) for i in range(a)] + [huge]
    t = [-huge] + [int(input()) for i in range(b)] + [huge]
    for i in range(q):
        x = int(input())
        b = bisect.bisect_right(s, x)
        d = bisect.bisect_right(t, x)
        res = huge
        for sh in s[b - 1:b + 1]:
            for te in t[d - 1:d + 1]:
                d1 = abs(sh - x) + abs(sh - te)
                d2 = abs(te - x) + abs(sh - te)
                res = min(res, d1, d2)
        print(res)


if __name__ == "__main__":
    main()
