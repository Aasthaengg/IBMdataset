import sys
import math
import collections
import bisect
import copy

# import numpy as np

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))
na1 = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))


# ===CODE===


def main():
    n = ni()
    yes = dict()
    for i in range(3, 1000):
        if (i * (i - 1)) % 2 == 0:
            yes[(i * (i - 1)) // 2] = [i, i - 1]
    tmp = max(yes)

    if n == 1:
        print("Yes")
        print(2)
        print(1, 1)
        print(1, 1)
        exit(0)


    if n not in yes.keys():
        print("No")
        exit(0)

    xl, xs = yes[n]

    ans = [[] for _ in range(xl)]
    cnt = 1
    idx = 0
    while xs >= 1:
        tmp = cnt
        for i in range(idx, min(xl, idx + 3)):
            for j in range(xs):
                if cnt == tmp + 3 * (xs - 1):
                    ans[i].append(tmp)
                    break
                else:
                    ans[i].append(cnt)
                if j != 0 and j != xs - 1:
                    ans[idx + 2 + j].append(cnt)
                if j != xs - 1:
                    cnt += 1
        idx += 3
        xs -= 3

    print("Yes")
    print(len(ans))
    for ansi in ans:
        print(len(ansi), *ansi, sep=" ")


if __name__ == '__main__':
    main()
