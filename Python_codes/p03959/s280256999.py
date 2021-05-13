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
    n = ni()
    l = na()
    r = na()

    res_l = [[0, False] for _ in range(n)]
    res_r = [[0, False] for _ in range(n)]

    checker = True

    tmp = 0
    for i, li in enumerate(l):
        if li > tmp:
            res_l[i] = li, True
        elif li == tmp:
            res_l[i][0] = tmp
        else:
            checker = False
            break
        tmp = li

    tmp = 0
    for i, ri in enumerate(reversed(r)):
        if ri > tmp:
            res_r[-1 - i] = ri, True
        elif ri == tmp:
            res_r[-1 - i][0] = tmp
        else:
            checker = False
            break
        tmp = ri

    res = [[0, False] for _ in range(n)]

    for i in range(n):
        if res_l[i][1] and res_r[i][1]:
            if res_l[i][0] != res_r[i][0]:
                checker = False
                break
            else:
                res[i] = res_l[i][0], True
        elif res_l[i][1] or res_r[i][1]:
            t_num = res_l[i][0] if res_l[i][1] else res_r[i][0]
            f_num = res_l[i][0] if not res_l[i][1] else res_r[i][0]
            if t_num > f_num:
                checker = False
                break
            else:
                res[i] = t_num, True
        else:
            res[i] = min(res_l[i][0], res_r[i][0]), False

    ans = 1
    for num, flg in res:
        if flg:
            continue
        ans *= num
        ans %= MOD

    print(ans if checker else 0)


if __name__ == '__main__':
    main()
