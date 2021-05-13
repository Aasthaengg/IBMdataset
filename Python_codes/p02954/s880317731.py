import sys
import itertools
input = lambda: sys.stdin.readline().rstrip()


def solve():

    S = input()
    N = len(S)
    gr = itertools.groupby(list(S))
    ans = [0 for _ in range(N)]

    s = 0
    for k, g in gr:
        g = list(g)
        if k == 'R':
            rlen = len(g)
        elif k == 'L':
            llen = len(g)
            if rlen % 2 == 0:
                ans[s + rlen - 1] += rlen // 2
                ans[s + rlen] += rlen // 2
            elif rlen % 2 == 1:
                ans[s + rlen - 1] += (rlen // 2) + 1
                ans[s + rlen] += rlen // 2
            if llen % 2 == 0:
                ans[s + rlen - 1] += llen // 2
                ans[s + rlen] += llen // 2
            elif llen % 2 == 1:
                ans[s + rlen - 1] += (llen // 2)
                ans[s + rlen] += (llen // 2) + 1
            s += rlen + llen

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    solve()
