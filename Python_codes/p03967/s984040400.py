import sys
import math
import collections
import bisect
import itertools

# import numpy as np

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline().rstrip())
ns = lambda: map(int, sys.stdin.readline().rstrip().split())
na = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
na1 = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().rstrip().split()))


# ===CODE===

def main():
    s = list(input())

    g = 0
    p = 0
    ans = 0

    for i in range(len(s)):
        if p + 1 <= g:
            a = "p"
            p += 1
        else:
            a = "g"
            g += 1

        if a == s[i]:
            continue
        elif a == "p":
            ans += 1
        else:
            ans -= 1

    print(ans)


if __name__ == '__main__':
    main()
