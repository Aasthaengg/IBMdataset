import sys

# import math
# import bisect

# import copy
# import heapq
# from collections import deque
# import decimal

# sys.setrecursionlimit(100001)
INF = sys.maxsize
# MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    n = ni()
    d1 = []
    d2 = []
    for i in range(n):
        t = sys.stdin.readline().split()
        tmp = "".join(t)
        d1.append(int(tmp))
    for i in range(n):
        d2.append(na())

    ans = -10**9
    for i in range(1, 2 ** 10):
        cost = 0
        for j in range(n):
            b = i & int(str(d1[j]),2)
            b = list(format(b, "b"))
            b = [int(n) for n in b]
            b = sum(b)
            cost += d2[j][b]

        ans = max(ans, cost)

    print(ans)


if __name__ == '__main__':
    main()
